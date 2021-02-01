from django.contrib.auth.decorators import login_required
from vendor.models import sellerProfile


@login_required(login_url='/login')
class SellerAccountMixin(object):
    account = None

    def get_account(self):
        user = self.request.user
        accounts = sellerProfile.objects.filter(user=user)
        if accounts.exists() and accounts.count() == 1:
            self.account = accounts.first()
            return accounts.first()
        return None
