from django.db import models


def string_filed(max_lenght):
    class _StringField(models.CharField):
        def __init__(self, *args, **kwargs):
            kwargs['max_length'] = max_lenght
            super().__init__(*args, **kwargs)
    return _StringField
