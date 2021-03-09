from django.contrib.auth.backends import ModelBackend
from core.models import Member

class ProxiedModelBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return Member.objects.get(pk=user_id)
        except:
            return None