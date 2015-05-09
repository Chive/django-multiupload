from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.UploadView.as_view()),
]
