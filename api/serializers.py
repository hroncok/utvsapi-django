import itertools

from rest_framework import serializers

from . import models


def fields(model):
    '''Get a generator of all field names of a model'''
    return (f.name for f in model._meta.fields)


def properties(model):
    '''Get a generator of all property names of a model except pk'''
    props = (n for n in dir(model) if isinstance(getattr(model, n), property))
    return (prop for prop in props if prop != 'pk')


def publics(model):
    '''Get names of all public fields and properties of a model'''
    both = itertools.chain(fields(model), properties(model))
    return tuple(name for name in both if not name.startswith('_'))


def serializer(model_):
    '''Get a default Serializer class for a model'''
    class _Serializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = model_
            fields = publics(model)
    return _Serializer


DestinationSerializer = serializer(models.Destination)
HallSerializer = serializer(models.Hall)
TeacherSerializer = serializer(models.Teacher)
SportSerializer = serializer(models.Sport)
CourseSerializer = serializer(models.Course)
EnrollmentSerializer = serializer(models.Enrollment)
