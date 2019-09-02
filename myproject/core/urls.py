from django.urls import path
from myproject.core import views as v


app_name = 'core'


urlpatterns = [
    path('', v.home, name='home'),
]
