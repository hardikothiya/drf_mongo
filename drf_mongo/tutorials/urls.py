from django.urls import re_path as url, path
from . import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    url(r'^api/tutorials$', views.TutorialList.as_view()),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.TutorialDetail.as_view()),
    url(r'^api/tutorials/published$', views.TutorialPublished.as_view()),
    path('docs', get_schema_view(
        title="DRF Mongo",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
]