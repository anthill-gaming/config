from anthill.platform.api.rest.handlers.detail import DetailMixin
from anthill.platform.api.rest.handlers.edit import (
    CreatingMixin, UpdatingMixin, DeletionMixin, ModelFormHandler)
from anthill.platform.api.rest.handlers.list import ListHandler
from config.models import ApplicationVersion, Build
from .forms import EditApplicationVersionBuildForm


class ApplicationVersionHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                                ModelFormHandler):
    """Multiple operations with application versions."""
    slug_url_kwarg = 'version'
    slug_field = 'app_version'

    def get_queryset(self):
        kwargs = dict(app_name=self.path_kwargs['name'])
        queryset = ApplicationVersion.query.filter_by(**kwargs)
        return queryset


class ApplicationVersionListHandler(ListHandler):
    """Get list of application versions."""
    def get_queryset(self):
        kwargs = dict(app_name=self.path_kwargs['name'])
        queryset = ApplicationVersion.query.filter_by(**kwargs)
        return queryset


class BuildHandler(CreatingMixin, UpdatingMixin, DeletionMixin, DetailMixin,
                   ModelFormHandler):
    """Multiple operations with builds."""
    queryset = Build.query.filter_by(enabled=True)


class BuildListHandler(ListHandler):
    """Get list of builds."""
    queryset = Build.query.filter_by(enabled=True)


class ApplicationVersionSetBuildHandler(UpdatingMixin, ModelFormHandler):
    slug_url_kwarg = 'version'
    slug_field = 'app_version'
    form_class = EditApplicationVersionBuildForm

    def get_queryset(self):
        kwargs = dict(app_name=self.path_kwargs['name'])
        queryset = ApplicationVersion.query.filter_by(**kwargs)
        return queryset


class ApplicationVersionDiscardBuildHandler(ModelFormHandler):
    slug_url_kwarg = 'version'
    slug_field = 'app_version'

    def get_queryset(self):
        kwargs = dict(app_name=self.path_kwargs['name'])
        queryset = ApplicationVersion.query.filter_by(**kwargs)
        return queryset

    async def put(self, *args, **kwargs):
        # noinspection PyAttributeOutsideInit
        self.object = await self.get_object()
        self.object.build_id = None
        await self.put(*args, **kwargs)
