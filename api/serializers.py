from . import models
from rest_framework import serializers


def serializer(mod):
    class _Serializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = mod
            fields = tuple(field.name for field in model._meta.fields)
    return _Serializer


DestinationSerializer = serializer(models.Destination)
HallSerializer = serializer(models.Hall)
TeacherSerializer = serializer(models.Teacher)
SportSerializer = serializer(models.Sport)
CourseSerializer = serializer(models.Course)
EnrollmentSerializer = serializer(models.Enrollment)
