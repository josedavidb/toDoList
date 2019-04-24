from django.conf.urls import url
from django.contrib import admin
from toDo.views import index
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
]