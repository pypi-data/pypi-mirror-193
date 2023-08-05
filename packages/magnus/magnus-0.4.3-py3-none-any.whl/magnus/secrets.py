import logging
import os
from functools import lru_cache
from typing import Union

from pydantic import BaseModel

from magnus import defaults, exceptions, utils

logger = logging.getLogger(defaults.NAME)


class BaseSecrets:
    """
    A base class for Secrets Handler.
    All implementations should extend this class.

    Note: As a general guideline, do not extract anything from the config to set class level attributes.
          Integration patterns modify the config after init to change behaviors.
          Access config properties using getters/property of the class.

    Raises:
        NotImplementedError: Base class and not implemented
    """
    service_name = ''

    class Config(BaseModel):
        pass

    def __init__(self, config: dict, **kwargs):  # pylint: disable=unused-argument
        config = config or {}
        self.config = self.Config(**config)

    def get(self, name: str = None, **kwargs) -> Union[str, dict]:
        """
        Return the secret by name.
        If no name is give, return all the secrets.

        Args:
            name (str): The name of the secret to return.

        Raises:
            NotImplementedError: Base class and hence not implemented.
        """
        raise NotImplementedError


class DoNothingSecretManager(BaseSecrets):
    """
    Does nothing secret manager
    """

    service_name = 'do-nothing'

    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.secrets = {}

    def get(self, name: str = None, **kwargs) -> Union[str, dict]:
        """
        If a name is provided, return None else return empty dict.

        Args:
            name (str): The name of the secret to retrieve

        Raises:
            Exception: If the secret by the name is not found.

        Returns:
            [type]: [description]
        """
        if name:
            return ''
        return {}


class EnvSecretsManager(BaseSecrets):
    """
    A secret manager via environment variables.

    This secret manager returns nothing if the key does not match
    """

    service_name = 'env-secrets-manager'

    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)

    def get(self, name: str = None, **kwargs) -> Union[str, dict]:
        """
        If a name is provided, we look for that in the environment.
        If a environment variable by that name is not found, we raise an Exception.

        If a name is not provided, we return an empty dictionary.

        Args:
            name (str): The name of the secret to retrieve

        Raises:
            Exception: If the secret by the name is not found.

        Returns:
            [type]: [description]
        """
        if name:
            try:
                return os.environ[name]
            except KeyError:
                raise exceptions.SecretNotFoundError(secret_name=name, secret_setting="environment")

        return {}


class DotEnvSecrets(BaseSecrets):
    """
    A secret manager which uses .env files for secrets.

    We recommend this secrets manager only for local development and should not be used for anything close to
    production.
    """

    service_name = 'dotenv'

    class Config(BaseModel):
        location: str = defaults.DOTENV_FILE_LOCATION

    def __init__(self, config, **kwargs):
        super().__init__(config, **kwargs)
        self.secrets = {}

    @property
    def secrets_location(self):
        """
        Return the location of the .env file.
        If the user has not over-ridden it, it defaults to .env file in the project root.

        Returns:
            str: The location of the secrets file
        """
        return self.config.location

    def _load_secrets(self):
        """
        We assume that a dotenv file is of format,
            key=value  -> secrets[key]='value'
            key1=value1# comment  -> secrets[key1]='value1'
            key2=value2 # comment. -> secrets[key2]='value2'

        We strip the secret value of any empty spaces at the start and end.

        Raises:
            Exception: If the file at secrets_location is not found.
            Exception: If the secrets are not formatted correctly.
        """
        secrets_location = self.secrets_location
        if not utils.does_file_exist(secrets_location):
            raise Exception(f'Did not find the secrets file in {secrets_location}')

        with open(secrets_location, 'r') as fr:
            for secret_line in fr:
                secret_line = secret_line.split('#')[0]  #  To remove any comments the user might have put
                data = secret_line.split('=')
                if len(data) != 2:
                    raise Exception('A secret should be of format, secret_name=secret_value[# any comment]')
                key, value = data
                self.secrets[key] = value.strip('\n')

    def get(self, name: str = None, **kwargs) -> Union[str, dict]:
        """
        Get a secret of name from the secrets file.

        If no name is provided, we return all

        Args:
            name (str): The name of the secret to retrieve

        Raises:
            Exception: If the secret by the name is not found.

        Returns:
            [type]: [description]
        """
        self._load_secrets()
        if not name:
            return self.secrets

        if name in self.secrets:
            return self.secrets[name]

        secrets_location = self.secrets_location
        raise exceptions.SecretNotFoundError(secret_name=name, secret_setting=secrets_location)
