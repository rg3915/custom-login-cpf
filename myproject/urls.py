from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from myproject.core import views as v


urlpatterns = [
    path('', include('myproject.core.urls', namespace='core')),
    path('myauth/', v.authenticate, name='authenticate'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
