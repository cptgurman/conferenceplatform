from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, u, timestamp):
        return (text_type(u.is_active) + text_type(u) + text_type(timestamp))


token_generator = AppTokenGenerator()
