# For more details about routing, see
# http://www.tornadoweb.org/en/stable/routing.html
from tornado.web import url
from . import handlers as h


route_patterns = [
    url(r'^/application/(?P<name>[^/]+)/version/?$', h.ApplicationVersionHandler, name='app_version_create'),
    url(r'^/application/(?P<name>[^/]+)/versions/?$', h.ApplicationVersionListHandler, name='app_versions'),
    url(r'^/application/(?P<name>[^/]+)/(?P<version>[^/]+)/?$', h.ApplicationVersionHandler, name='app_version'),

    url(r'^/build/(?P<id>[^/]+)/?$', h.BuildHandler, name='build'),
    url(r'^/build/?$', h.BuildHandler, name='build_create'),
    url(r'^/builds/?$', h.BuildListHandler, name='builds'),
]
