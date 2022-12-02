from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/tutorials$', views.TutorialList.as_view()),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.TutorialDetail.as_view()),
    url(r'^api/tutorials/published$', views.TutorialPublished.as_view())
]