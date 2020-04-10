# -*- coding: utf-8 -*-
"""
Provides eventtypes.conf parsing mechanism
"""

class EventTypeParser(object):
    """
    Parses eventtypes.conf and extracts eventtypes  
    Args:
        splunk_app_path (str): Path of the Splunk app
        app (splunk_appinspect.App): Object of Splunk app
    """
    def __init__(self, splunk_app_path, app):
        self.app = app 
        self.splunk_app_path = splunk_app_path
        self.eventtypes = self.app.eventtypes_conf()

    def get_eventtypes(self):
        """
        Parse the App configuration files & yield eventtypes
        
        Yields:
            generator of list of eventtypes
        """
        for eventtype_section in self.eventtypes.sects:
            yield {
                "stanza": eventtype_section
            }
