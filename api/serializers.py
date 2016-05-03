from . import models
from rest_framework import serializers


def public_fields(model):
    return tuple(
        f.name for f in model._meta.fields if not f.name.startswith('_'))


def serializer(mod):
    class _Serializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = mod
            fields = public_fields(model)
    return _Serializer


DestinationSerializer = serializer(models.Destination)
HallSerializer = serializer(models.Hall)
TeacherSerializer = serializer(models.Teacher)
SportSerializer = serializer(models.Sport)
CourseSerializer = serializer(models.Course)
EnrollmentSerializer = serializer(models.Enrollment)
