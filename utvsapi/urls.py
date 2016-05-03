from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'destinations', views.DestinationViewSet)
router.register(r'halls', views.HallViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'sports', views.SportViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'enrollments', views.EnrollmentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
