"""
SshProvider is a class that provides a way to execute SSH commands and get the output.
"""
import dataclasses
import io

import pydantic
from paramiko import AutoAddPolicy, RSAKey, SSHClient

from keep.exceptions.provider_config_exception import ProviderConfigException
from keep.providers.base.base_provider import BaseProvider
from keep.providers.models.provider_config import ProviderConfig
from keep.providers.providers_factory import ProvidersFactory


@pydantic.dataclasses.dataclass
class SshProviderAuthConfig:
    """SSH authentication configuration.

    Raises:
        ValueError: pkey and password are both empty

    """

    # TODO: validate hostname because it seems pydantic doesn't have a validator for it
    host: str = dataclasses.field(
        metadata={"required": True, "description": "SSH hostname"}
    )
    user: str = dataclasses.field(
        metadata={"required": True, "description": "SSH user"}
    )
    port: int = dataclasses.field(
        default=22, metadata={"required": False, "description": "SSH port"}
    )
    pkey: str = dataclasses.field(
        default="", metadata={"required": False, "description": "SSH private key"}
    )
    password: str = dataclasses.field(
        default="", metadata={"required": False, "description": "SSH password"}
    )

    @pydantic.root_validator
    def check_password_or_pkey(cls, values):
        password, pkey = values.get("password"), values.get("pkey")
        if password == "" and pkey == "":
            raise ValueError("either password or pkey must be provided")
        return values


class SshProvider(BaseProvider):
    def __init__(self, provider_id: str, config: ProviderConfig):
        super().__init__(provider_id, config)
        self.client = self.__generate_client()

    def __generate_client(self) -> SSHClient:
        """
        Generates a paramiko SSH connection.

        Returns:
            SSHClient: The connection to the SSH server.
        """
        ssh_client = SSHClient()
        ssh_client.set_missing_host_key_policy(AutoAddPolicy())

        host = self.authentication_config.host
        port = self.authentication_config.port
        user = self.authentication_config.user

        private_key = self.authentication_config.pkey
        if private_key:
            # Connect using private key
            private_key_file = io.StringIO(private_key)
            private_key_file.seek(0)
            key = RSAKey.from_private_key(
                private_key_file, self.config.authentication.get("pkey_passphrase")
            )
            ssh_client.connect(host, port, user, pk=key)
        else:
            # Connect using password
            ssh_client.connect(
                host,
                port,
                user,
                self.authentication_config.password,
            )

        return ssh_client

    def dispose(self):
        """
        Closes the SSH connection.
        """
        try:
            self.client.close()
        except Exception as e:
            self.logger.error("Error closing SSH connection", extra={"error": str(e)})

    def validate_config(self):
        """
        Validates required configuration for SSH provider.

        """
        self.authentication_config = SshProviderAuthConfig(**self.config.authentication)

    def query(self, **kwargs: dict):
        """
        Query snowflake using the given query

        Args:
            query (str): command to execute

        Returns:
            list: of the results for the executed command.
        """
        command = kwargs.pop("command")
        stdin, stdout, stderr = self.client.exec_command(command.format(**kwargs))
        stdout.channel.set_combine_stderr(True)
        return stdout.readlines()


if __name__ == "__main__":
    # Output debug messages
    import logging

    logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])

    # Load environment variables
    import os

    user = os.environ.get("SSH_USERNAME")
    password = os.environ.get("SSH_PASSWORD")
    host = os.environ.get("SSH_HOST")

    config = {
        "id": "ssh-demo",
        "authentication": {
            "user": user,
            "password": password,
            "host": host,
        },
    }
    provider = ProvidersFactory.get_provider(
        provider_type="ssh", provider_config=config
    )
    result = provider.query("df -h")
    print(result)
