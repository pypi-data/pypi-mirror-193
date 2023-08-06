import json
import requests
import yaml


class ArgusConfiguration(object):
    def __init__(self, config_input):
        # Default config params
        self._config = {
            'authentication': None,
            'suites': None,
            'validation': None,
            'validator': None
        }

        # Load config
        self._configuration_input = config_input

        if isinstance(config_input, dict):
            self._config = config_input
        else:
            self._config = self._get_dictionary_from_file(config_input)

        self._validate_configuration(self._config)

    @staticmethod
    def _get_dictionary_from_file(config_fpath):
        try:
            config_fhand = open(config_fpath, 'r')
        except IOError:
            msg = 'Unable to read file "' + config_fpath + '"'
            raise IOError(msg)

        config_dict = None
        if config_fpath.endswith('.yml') or config_fpath.endswith('.yaml'):
            config_dict = yaml.safe_load(config_fhand)

        if config_fpath.endswith('.json'):
            config_dict = json.loads(config_fhand.read())

        config_fhand.close()

        return config_dict

    @staticmethod
    def _validate_configuration(config):
        if config is None:
            raise ValueError('Missing configuration dictionary')

    @property
    def suites(self):
        return self._config['suites']

    @suites.setter
    def suites(self, new_suites):
        self._config['suites'] = new_suites

    @property
    def authentication(self):
        return self._config['authentication']

    @authentication.setter
    def authentication(self, new_authentication):
        self._config['authentication'] = new_authentication
