import os
from dataclasses import dataclass, field
from typing import Any, ClassVar, Dict, Optional, Sequence

from aws_cdk import Environment, aws_apigateway, aws_lambda


@dataclass(frozen=True)
class LambdaDefaults:
    memory_size: int = 128
    timeout: int = 25
    reserved_concurrent_executions: Optional[int] = None
    env_variables: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Configuration:
    env_name: str
    app_name: str
    # see https://docs.aws.amazon.com/cdk/v2/guide/environments.html
    env: Environment
    python_version: aws_lambda.Runtime
    # lambda config
    lambda_defaults: LambdaDefaults = LambdaDefaults()
    # vpc config
    vpc_id: Optional[str] = None
    security_group_id: Optional[str] = None
    subnets_ids: Optional[Sequence[str]] = None
    allow_public_subnet: bool = False
    # cors see: https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_apigateway-readme.html#cross-origin-resource-sharing-cors
    default_cors_options: Optional[aws_apigateway.CorsOptions] = None
    # X-Ray tracing
    active_tracing: bool = False

    __configs__: ClassVar[Dict[str, "Configuration"]] = {}

    def __post_init__(self) -> None:
        if self.env_name.lower() in self.__configs__:
            raise ValueError(
                f"Configuration with env_name '{self.env_name}' already exists."
            )
        self.__configs__[self.env_name.lower()] = self
        self._validate_vpc_config()

    def _validate_vpc_config(self) -> None:
        if self.vpc_id:
            assert self.security_group_id, "security_group_id not provided"
            assert self.subnets_ids, "subnets_ids not provided"

    @classmethod
    def get_configuration(cls) -> "Configuration":
        __import__("config")  # hack to import configurations from config.py
        env_name = os.getenv("ENV", "")
        config = cls.__configs__.get(env_name.lower())  # type: ignore
        if not config:
            raise ValueError(f"No config with env_name='{env_name}'.")
        return config
