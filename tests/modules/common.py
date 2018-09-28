##
## Python 2.7.X -> 3.0.X
### Common testing lib
### Author: Isham J. Araia @ None
### Date: 10 - 09 - 2018

import yaml

class Common():
    """
    Base class contains basic and general modules.
    """

    def __init__(self, config):
        """
        Constructor method.
        Load general config
        """
        with open(config, 'r') as stream:
            try:
                self.CONFIG = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
