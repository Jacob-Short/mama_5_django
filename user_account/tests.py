from django.contrib.auth.base_user import BaseUserManager
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            'testuser@super.com', 'password'
        )
        self.assertEqual(super_user.email, 'testuser@super.com')
        self.assertEqual(super_user.password, 'password')
        self.assertEqual(super_user.is_superuser)
        self.assertEqual(super_user.is_staff)
        self.assertEqual(super_user.is_active)
        self.assertEqual(str(super_user), 'email')

        objects = BaseUserManager

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = 'email'

        def __str__(self):
            return self.email