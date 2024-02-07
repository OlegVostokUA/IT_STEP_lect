from django.urls import re_path
from . import views
from django.conf.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet)


urlpatterns = [
    re_path(r'^subjects/$', views.SubjectListView.as_view(), name='subject_list'),
    re_path(r'^subjects/(?P<pk>\d+)/$', views.SubjectDetailView.as_view(), name='subject_detail'),
    re_path(r'^courses/(?P<pk>\d+)/enroll/$', views.CourseEnrollView.as_view(), name='course_enroll'),
    re_path(r'^', include(router.urls)),
]
