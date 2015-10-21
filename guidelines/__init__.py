"""
Plugin definition for the guidelines OPAL plugin
"""
from opal.core import plugins

from guidelines import api
from guidelines.urls import urlpatterns

class GuidelinesPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our OPAL application.
    """
    urls = urlpatterns
    javascripts = {
        'opal.controllers': [
            'js/guidelines/controllers/select_guideline.js'
        ],
        # Add your javascripts here!
        'opal.guidelines': [
            # 'js/guidelines/app.js',
            # 'js/guidelines/controllers/larry.js',
            # 'js/guidelines/services/larry.js',
        ]
    }

    apis = [
        ('guideline', api.GuidelineViewSet),
        ('guideline_consultation', api.ConsultationViewSet)
    ]        

    def restricted_teams(self, user):
        """
        Return any restricted teams for particualr users that our
        plugin may define.
        """
        return []

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def flows(self):
        """
        Return any custom flows that our plugin may define
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}

    
plugins.register(GuidelinesPlugin)

