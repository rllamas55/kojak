from django.conf.urls import url
from basic_app import views

#template URLs
app_name = 'basic_app'

urlpatterns = [
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
]
