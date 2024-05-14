from extractors.configs.extraction_config.prompt_config import extraction_configurations, extraction_configurations_eng

class ConfigHandler:
    """
    A class used to handle configuration for data extraction.

    ...

    Attributes
    ----------
    general_config : dict
        A dictionary holding the general extraction configurations.
    tenant_general_config : dict
        A dictionary holding the tenant-specific general configurations.
    tenant_extractor_config : dict
        A dictionary holding the tenant-extractor-specific configurations.
    extractor_config : dict
        A dictionary holding the final extractor configurations.

    Methods
    -------
    create_config():
        Assigns values to the extractor_config dictionary.
    assign_value(config: dict):
        Updates the extractor_config dictionary with values from a given config dictionary.
    """

    def __init__(self, tenant='general', extraction='general', language='it'):
        """
        Constructs all the necessary attributes for the ConfigHandler object.

        Parameters
        ----------
            tenant : str, optional
                The tenant for which the extraction is being done (default is 'general').
            extraction : str, optional
                The extraction type (default is 'general').
        """
        # Language selection
        if language not in ['it', 'en', 'fr', 'de', 'es']:
            raise ValueError('Language not supported')
        elif language == 'en':
            extraction_config = extraction_configurations_eng
        else:
            extraction_config = extraction_configurations

        self.general_config = extraction_config['general']
        if tenant !='general':
            self.tenant_general_config = extraction_config[tenant]['general']
            self.tenant_extractor_config = extraction_config[tenant][extraction]
        else:
            self.tenant_general_config, self.tenant_extractor_config= {}, {}

        self.extractor_config = {
            "word_representation": {},
            "prompt": {},
            "tag": {}
        }
        self.create_config()

    def create_config(self):
        """
        Calls the assign_value method for general_config, tenant_general_config, and tenant_extractor_config.
        """
        self.assign_value(self.general_config)
        self.assign_value(self.tenant_general_config)
        self.assign_value(self.tenant_extractor_config)

    def assign_value(self, config):
        """
        Updates the extractor_config dictionary with values from a given config dictionary.

        Parameters
        ----------
            config : dict
                A dictionary containing the configuration values.
        """
        for key, value in config.items():
            if key in self.extractor_config:
                self.extractor_config[key].update(value)
            else:
                self.extractor_config[key] = value

