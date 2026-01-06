from django.urls import path
from.views import *
urlpatterns = [
    path('login/',view=login_view,name='login view')
]
