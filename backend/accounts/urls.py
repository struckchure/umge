from django.urls import path

from accounts.api import (
    UserRegister,
    UserLogin,
    UserLogout
)

app_name = 'accounts'

urlpatterns = [
    path('account/register/', UserRegister.as_view()),
    path('account/login/', UserLogin.as_view()),
    path('account/logout/', UserLogout.as_view())
]
