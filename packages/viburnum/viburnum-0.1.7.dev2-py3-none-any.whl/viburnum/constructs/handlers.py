from dataclasses import dataclass
from typing import Dict, Optional, Sequence, Type

from aws_cdk import (
    Duration,
    aws_apigateway,
    aws_events,
    aws_events_targets,
    aws_lambda,
    aws_lambda_event_sources,
    aws_sqs,
)
from constructs import Construct

from viburnum.constructs.schemas import SchemaModel
from viburnum.constructs.stacks import AppStack


@dataclass(kw_only=True)
class HandlerProps:
    code_path: str
    handler: str
    reserved_concurrent_executions: Optional[int] = None
    memory: Optional[int] = None
    timeout: Optional[int] = None


class HandlerConstruct(Construct):
    def __init__(self, scope: "AppStack", id: str, handler_props: HandlerProps) -> None:
        super().__init__(scope, id)
        self.lambda_ = aws_lambda.Function(
            self,
            "Handler",
            code=aws_lambda.Code.from_asset(
                path=handler_props.code_path,
            ),
            runtime=scope.config.python_version,
            handler=handler_props.handler,
            layers=scope.common_layers,
            **scope.vpc_config,
            **self.__get_lambda_config(scope, handler_props),
            tracing=aws_lambda.Tracing.ACTIVE
            if scope.config.active_tracing
            else aws_lambda.Tracing.DISABLED,
        )

    def __get_lambda_config(self, scope: "AppStack", props: HandlerProps) -> dict:
        return {
            "reserved_concurrent_executions": props.reserved_concurrent_executions
            or scope.config.lambda_defaults.reserved_concurrent_executions,
            "memory_size": props.memory or scope.config.lambda_defaults.memory_size,
            "timeout": Duration.seconds(
                props.timeout or scope.config.lambda_defaults.timeout
            ),
        }


@dataclass(kw_only=True)
class RestApiHandlerProps(HandlerProps):
    path: str
    methods: list[str]
    request_model: Optional[Type[SchemaModel]] = None
    response_models: Optional[dict[int, Type[SchemaModel]]] = None


class RestApiHandler(HandlerConstruct):
    def __init__(
        self,
        scope: "AppStack",
        id: str,
        props: RestApiHandlerProps,
    ) -> None:
        super().__init__(scope, id, props)
        self._scope = scope
        self._props = props
        self._build_method()

    def _build_method(self):
        integration = aws_apigateway.LambdaIntegration(self.lambda_, allow_test_invoke=False)  # type: ignore

        self.endpoint = self._scope.api.root
        for path_part in (p for p in self._props.path.split("/") if p):
            self.endpoint = self.endpoint.get_resource(
                path_part
            ) or self.endpoint.add_resource(path_part)
        for method in self._props.methods:
            self.endpoint.add_method(
                method,
                integration,
                request_validator=self._get_request_validator(),  # type: ignore
                request_models=self._get_request_models(),
                # request_parameters=,
                method_responses=self._get_response_models(),
            )

    def _get_response_models(self) -> Sequence[aws_apigateway.MethodResponse]:
        responses = []
        if not self._props.response_models:
            return responses
        for status_code, response_model in self._props.response_models.items():
            # get model by name
            model = aws_apigateway.Model.from_model_name(
                self, f"ResponseModel{status_code}", response_model.__name__
            )
            # create method response
            responses.append(
                aws_apigateway.MethodResponse(
                    status_code=str(status_code),
                    response_models={"application/json": model},
                )
            )
        return responses

    def _get_request_validator(self) -> Optional[aws_apigateway.RequestValidator]:
        if self._props.request_model:
            return self._scope.request_validators["full"]
        return None

    def _get_request_models(self) -> Dict[str, aws_apigateway.IModel]:
        if not self._props.request_model:
            return {}
        model = aws_apigateway.Model.from_model_name(
            self, "RequestModel", self._props.request_model.__name__
        )
        return {"application/json": model}


@dataclass(kw_only=True)
class ScheduledEventHandlerProps(HandlerProps):
    expression: str


class ScheduledEventHandler(HandlerConstruct):
    def __init__(
        self, scope: "AppStack", id: str, handler_props: ScheduledEventHandlerProps
    ) -> None:
        super().__init__(scope, id, handler_props)
        self.rule = aws_events.Rule(
            self,
            "Event",
            schedule=aws_events.Schedule.expression(handler_props.expression),
            targets=[aws_events_targets.LambdaFunction(self.lambda_)],  # type: ignore
        )


@dataclass(kw_only=True)
class SqsHandlerProps(HandlerProps):
    report_batch_item_failures: bool = True
    batch_size: int = 10


class SqsHandler(HandlerConstruct):
    def __init__(
        self,
        scope: "AppStack",
        id: str,
        handler_props: SqsHandlerProps,
        queue: aws_sqs.Queue,
    ) -> None:
        super().__init__(scope, id, handler_props)
        self.queue = queue
        _sqs_event_source = aws_lambda_event_sources.SqsEventSource(
            self.queue,
            report_batch_item_failures=handler_props.report_batch_item_failures,
            batch_size=handler_props.batch_size,
        )
        self.lambda_.add_event_source(_sqs_event_source)
