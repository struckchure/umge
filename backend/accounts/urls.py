from django.urls import path

from accounts.api import (
    UserDetails,
    UserRegister,
    UserLogin,
    UserLogout,
    UserUpdate
)
from accounts.admin_api import AdminUserList

app_name = 'accounts'

urlpatterns = [
    path('account/', UserDetails.as_view()),
    path('account/register/', UserRegister.as_view()),
    path('account/login/', UserLogin.as_view()),
    path('account/logout/', UserLogout.as_view()),
    path('account/update/', UserUpdate.as_view()),

    path('account/admin/users/list/', AdminUserList.as_view())
]
