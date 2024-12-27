from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewSet, CourseViewSet

router = DefaultRouter()
router.register('students', StudentViewSet)
router.register('teachers', TeacherViewSet)
router.register('courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
