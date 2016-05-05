from rest_framework import viewsets
from drf_hal_json import views

from . import models, serializers, permissions
from .classproperty import classproperty


class FilterAllFieldsMixin:
    @classproperty
    def filter_fields(cls):
        model = cls.serializer_class.Meta.model
        return serializers.fields(model)


base = (viewsets.ReadOnlyModelViewSet, FilterAllFieldsMixin)


class DestinationViewSet(*base):
    '''
    API endpoint that allows destinations to be viewed.
    '''
    queryset = models.Destination.objects.all()
    serializer_class = serializers.DestinationSerializer


class HallViewSet(*base):
    '''
    API endpoint that allows halls to be viewed.
    '''
    queryset = models.Hall.objects.all()
    serializer_class = serializers.HallSerializer


class TeacherViewSet(*base):
    '''
    API endpoint that allows teachers to be viewed.
    '''
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer


class SportViewSet(*base):
    '''
    API endpoint that allows sports to be viewed.
    '''
    queryset = models.Sport.objects.all()
    serializer_class = serializers.SportSerializer


class CourseViewSet(*base):
    '''
    API endpoint that allows courses to be viewed.
    '''
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer


class EnrollmentViewSet(*base):
    '''
    API endpoint that allows enrollments to be viewed.
    '''
    queryset = models.Enrollment.objects.all()
    serializer_class = serializers.EnrollmentSerializer
