from anthill.platform.api.rest.handlers.detail import DetailMixin
from anthill.platform.api.rest.handlers.edit import (
    CreatingMixin, UpdatingMixin, DeletionMixin, ModelFormHandler)
from anthill.platform.api.rest.handlers.list import ListHandler
from config.models import ApplicationVersion, Build


class ApplicationVersionHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                                ModelFormHandler):
    """Multiple operations with application versions."""
    slug_url_kwarg = 'version'
    slug_field = 'app_version'

    def get_queryset(self):
        kwargs = dict(name=self.path_kwargs['name'])
        queryset = ApplicationVersion.query.filter_by(**kwargs)
        return queryset


class ApplicationVersionListHandler(ListHandler):
    """Get list of application versions."""
    def get_queryset(self):
        kwargs = dict(name=self.path_kwargs['name'])
        queryset = ApplicationVersion.query.filter_by(**kwargs)
        return queryset


class BuildHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                   ModelFormHandler):
    """Multiple operations with builds."""
    queryset = Build.query.filter_by(enabled=True)


class BuildListHandler(ListHandler):
    """Get list of builds."""
    queryset = Build.query.filter_by(enabled=True)
