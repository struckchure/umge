from django.urls import path

from accounts.api import (
    UserDetails,
    UserRegister,
    UserLogin,
    UserLogout,
    UserUpdate,
    FundWallet
)
from accounts.admin_api import (
    AdminUserList,
    AdminRiderList
)

app_name = 'accounts'

urlpatterns = [
    path('account/', UserDetails.as_view()),
    path('account/register/', UserRegister.as_view()),
    path('account/login/', UserLogin.as_view()),
    path('account/logout/', UserLogout.as_view()),
    path('account/update/', UserUpdate.as_view()),

    path('account/wallet/fund/', FundWallet.as_view()),

    path('account/admin/users/', AdminUserList.as_view()),
    path('account/admin/riders/', AdminRiderList.as_view()),
]
