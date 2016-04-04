from __future__ import absolute_import, unicode_literals

import logging
import os

from mopidy import config, exceptions, ext


__version__ = '0.1'

# If you need to log, use loggers named after the current Python module
logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-Webtouch'
    ext_name = 'webtouch'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        return schema

    '''def get_command(self):
        from .commands import SoundspotCommand
        return SoundspotCommand()'''

    def validate_environment(self):
        # Any manual checks of the environment to fail early.
        # Dependencies described by setup.py are checked by Mopidy, so you
        # should not check their presence here.
        pass

    def setup(self, registry):
        registry.add('http:app', {'name': self.ext_name, 'factory': self.factory})

    def factory(self, config, core):
        from tornado.web import RedirectHandler
        from .web import IndexHandler, StaticHandler
        path = os.path.join(os.path.dirname(__file__), 'static')
        return [
            (r'/', RedirectHandler, {'url': 'index.html'}),
            (r'/(index.html)', IndexHandler, {'config': config, 'path': path}),
            (r'/(.*)', StaticHandler, {'path': path})
        ]