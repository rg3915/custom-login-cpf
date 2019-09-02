from django.contrib import admin
from django.urls import include, path
from myproject.core import views as v


urlpatterns = [
    path('', include('myproject.core.urls', namespace='core')),
    path('admin/', admin.site.urls),
]
