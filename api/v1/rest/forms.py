from anthill.framework.forms.orm import (
    ModelForm, ModelUpdateForm, ModelCreateForm, ModelSearchForm)
from config.models import ApplicationVersion


class EditApplicationVersionBuildForm(ModelForm):
    class Meta:
        model = ApplicationVersion
        include = ['build_id']
