from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class UserInfo(models.Model):
    user_type_choices = {
        (1, '普通用户'),
        (2, 'VIP'),
        (3, 'SVIP'),
    }
    username = models.CharField(max_length=32)
    password_hash = models.CharField(max_length=255)
    user_type = models.IntegerField(choices=user_type_choices, default=1)

    @staticmethod
    def make_password(plain_password):
        return make_password(plain_password, hasher='pbkdf2_sha256')

    def verify_password(self, plain_password):
        return check_password(plain_password, self.password_hash)

    class Meta:
        db_table = 'userinfo'


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
    expire_in = models.IntegerField()

    class Meta:
        db_table = 'usertoken'
