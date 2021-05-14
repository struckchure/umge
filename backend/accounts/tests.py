from django.test import TestCase
from accounts.models import User, Wallet
from cart.models import Cart

'''
Test default user types
Test default permissions levels
Test that user wallet and cart is created
'''

user_details = {
    'username': 'beta-tester'
}


class UserTestCase(TestCase):

    def setUp(self):
        User.objects.create(
            **user_details
        )

    def test_permissions_and_types(self):
        user = User.objects.get(
            **user_details
        )

        self.assertEqual(user.is_superuser, False)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.type, User.Types.NORMAL)

    def test_get_cart(self):
        user = User.objects.get(
            **user_details
        )

        user_cart = Cart.objects.get(
            cart_user=user
        )

        self.assertEqual(user.get_cart(), user_cart)

    def test_get_wallet(self):
        user = User.objects.get(
            **user_details
        )

        user_wallet = Wallet.objects.get(
            wallet_user=user
        )

        self.assertEqual(user.get_wallet(), user_wallet)

    def test_wallet(self):
        user = User.objects.get(
            **user_details
        )

        user_wallet = Wallet.objects.get(
            wallet_user=user
        )

        self.assertEqual(user_wallet.wallet_balance, 0)

    def test_fund_wallet(self):
        user = User.objects.get(
            **user_details
        )

        user_wallet = Wallet.objects.get(
            wallet_user=user
        )
        fund_wallet = user_wallet.fund_wallet(100)[1]

        self.assertEqual(fund_wallet, True)
