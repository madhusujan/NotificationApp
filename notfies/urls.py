from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$',views.index, name='notfies.html'),

#notfies/21
url(r'^(?P<lists>[0-9]+)/$', views.detail, name= 'detail'),
]

# url(r'^(?P<name>[0-9]+)$', views.detail, name)
