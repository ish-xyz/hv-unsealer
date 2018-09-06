## 
#### Common methods
#### August 2018 - Isham J. Araia

import re
import sys
import logging as log

class Common():
    """
    Class used to wrap all the common methods
    """
    
    def _valid_url(self, host):

        """
        Check if the URL syntax it's valid.
        """

        cpattern = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'test|' #test...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        if re.match(cpattern, host) == None:
            return False
        else: 
            return True

    def log(self, message, level):
        """
        Method used to log across all the package.
        Lv -> 1 INFO
        Lv -> 2 WARN
        Lv -> 3 ERR
        Lv -> 4 CRITICAL
        """

        if not message or not level:
            message = '2 valid arguments are required: "message" and "level". See help().'
            level = 4
        
        lvs = {
            1 : "INFO", 
            2 : "WARN",
            3 : "ERR",
            4 : "CRITICAL"
        }

        date = '00-00-00'
        stm = "{}: {} - {}".format(date, message, lvs[level])
        print(stm)
        return True
