from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.user_login,name='login'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^register/',views.register),
    url(r'^test/',views.login_test),
        ]
