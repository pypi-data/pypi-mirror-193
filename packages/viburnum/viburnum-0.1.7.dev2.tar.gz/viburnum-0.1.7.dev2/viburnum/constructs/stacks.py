import json
import logging
import os
import shutil
from functools import cached_property
from pathlib import Path
from typing import Dict

from aws_cdk import NestedStack, Stack, aws_apigateway, aws_ec2, aws_lambda_python_alpha
from constructs import Construct
from msgspec.json import schema_components

from viburnum.constructs.schemas import SchemaModel
from viburnum.deployer.configuration import Configuration


class AppStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        self.config = Configuration.get_configuration()
        super().__init__(scope, construct_id, env=self.config.env, **kwargs)

        self.handlers: dict = {}
        self.common_layers: list = []

        self.request_validators: Dict[str, aws_apigateway.RequestValidator] = {}
        self.request_validators["params"] = aws_apigateway.RequestValidator(
            self,
            "ParamsValidator",
            rest_api=self.api,
            validate_request_body=False,
            validate_request_parameters=True,
        )
        self.request_validators["full"] = aws_apigateway.RequestValidator(
            self,
            "FullValidator",
            rest_api=self.api,
            validate_request_body=True,
            validate_request_parameters=True,
        )

        self.__build_layers()
        self.__build_models()

    def __build_layers(self):
        layers_folder = Path("./.layers")
        if not layers_folder.exists():
            os.mkdir(str(layers_folder))

        if Path("./shared").exists():
            self.__build_shared_layer()
        self.__build_lib_layer()

    def __prepare_shared_layer(self):
        logging.info("Preparing shared layer")
        shared_layer_folder = Path("./.layers/shared")
        if os.path.exists(shared_layer_folder):
            shutil.rmtree(shared_layer_folder)
        os.mkdir(shared_layer_folder)
        shutil.copytree("shared", str(shared_layer_folder.joinpath("shared")))

    def __prepare_libraries_layer(self):
        # TODO: create requirements only if requirements.txt was changed
        logging.info("Preparing libraries layer")
        lib_layer_folder = Path("./.layers/lib")
        if os.path.exists(lib_layer_folder):
            shutil.rmtree(lib_layer_folder)
        os.mkdir(lib_layer_folder)
        shutil.copy("requirements.txt", str(lib_layer_folder))

    def __build_shared_layer(self):
        self.__prepare_shared_layer()
        self._shared_layer = aws_lambda_python_alpha.PythonLayerVersion(
            self,
            "SharedLayer",
            entry=str(Path("./.layers/shared")),
            compatible_runtimes=[self.config.python_version],
        )
        self.common_layers.append(self._shared_layer)

    def __build_lib_layer(self):
        self.__prepare_libraries_layer()
        self._lib_layer = aws_lambda_python_alpha.PythonLayerVersion(
            self,
            "LibLayer",
            entry=str(Path("./.layers/lib")),
            compatible_runtimes=[self.config.python_version],
        )
        self.common_layers.append(self._lib_layer)

    def __build_models(self):
        # mgspec
        ref_link = (
            f"https://apigateway.amazonaws.com/restapis/{self.api.rest_api_id}/models"
        )
        definitions = schema_components(
            SchemaModel.__schemas__.values(),
            ref_template="__spec_ref__/{name}",
        )[-1]
        # hack to replace #ref with api gateway specific reference
        definitions = json.loads(
            json.dumps(definitions).replace("__spec_ref__", ref_link)
        )
        # create Cfn models
        for name, schema_ in definitions.items():
            self.__create_cfn_model(name, schema_)

    def __create_cfn_model(self, name: str, schema_: dict):
        # call hook for schema customization
        schema_["$schema"] = "http://json-schema.org/draft-04/schema#"
        schema_ = SchemaModel.__schemas__[name].customize_schema(schema_)
        # create CfnModel
        aws_apigateway.CfnModel(
            self,
            f"Cfn{name}",
            rest_api_id=self.api.rest_api_id,
            # // the properties below are optional
            content_type="application/json",
            description="some description",
            name=name,
            schema=schema_,
        )

    @cached_property
    def api(self) -> aws_apigateway.RestApi:
        return aws_apigateway.RestApi(
            self,
            f"{self.config.app_name}RestApi",
            deploy=True,
            deploy_options=aws_apigateway.StageOptions(
                stage_name=self.config.env_name,
                tracing_enabled=self.config.active_tracing,
            ),
            default_cors_preflight_options=self.config.default_cors_options,
        )

    @cached_property
    def vpc_config(self) -> dict:
        """Return default vpc config for Lambda

        Returns:
            dict: vpc configuration
        """
        vpc_config = {}
        if self.config.vpc_id:
            vpc_config.update(
                {
                    "vpc": aws_ec2.Vpc.from_lookup(
                        self,
                        "VPC",
                        vpc_id=self.config.vpc_id,
                    ),
                    "vpc_subnets": aws_ec2.SubnetSelection(
                        subnets=[
                            aws_ec2.Subnet.from_subnet_id(self, f"Subnet{i}", s_id)
                            for i, s_id in enumerate(self.config.subnets_ids, start=1)  # type: ignore
                        ]
                    ),
                    "security_groups": [
                        aws_ec2.SecurityGroup.from_lookup_by_id(
                            self,
                            "LambdaSecurityGroup",
                            self.config.security_group_id,  # type: ignore
                        )
                    ],
                    "allow_public_subnet": self.config.allow_public_subnet,
                }
            )
        return vpc_config


class AppNestedStack(NestedStack):
    @property
    def api(self) -> aws_apigateway.RestApi:
        return self.nested_stack_parent.api  # type: ignore

    @property
    def vpc_config(self) -> dict:
        return self.nested_stack_parent.vpc_config  # type: ignore

    @property
    def config(self) -> Configuration:
        return self.nested_stack_parent.config  # type: ignore

    @property
    def common_layers(self) -> list:
        return self.nested_stack_parent.common_layers  # type: ignore

    @property
    def handlers(self) -> list:
        return self.nested_stack_parent.handlers  # type: ignore

    @property
    def request_validators(self) -> Dict[str, aws_apigateway.RequestValidator]:
        return self.nested_stack_parent.request_validators  # type: ignore
