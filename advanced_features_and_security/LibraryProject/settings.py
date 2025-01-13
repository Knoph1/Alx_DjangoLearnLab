AUTH_USER_MODEL = 'accounts.CustomUser'
from django.conf import settings
user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTH_USER_MODEL = 'bookshelf.CustomUser'
