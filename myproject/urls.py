from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

from myproject.core.forms import LoginForm

urlpatterns = [
    path('', include('myproject.core.urls', namespace='core')),
    path(
        'login/',
        LoginView.as_view(
            template_name='core/auth.html', authentication_form=LoginForm
        ),
        name='authenticate'
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
