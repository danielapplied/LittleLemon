from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from . import views

urlpatterns = [
    path('items', MenuItemsView.as_view()),
    path('items/<int:pk>', MenuItemDetailView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]