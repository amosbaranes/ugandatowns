from django.urls import path
from .views import index

app_name = 'openvidu'

urlpatterns = [
    path('', index, name='index'),
]
