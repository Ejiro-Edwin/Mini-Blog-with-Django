
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('posts.urls')),
    url('admin/', admin.site.urls),
    url('posts/', include('posts.urls')),
]
