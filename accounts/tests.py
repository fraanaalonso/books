from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomerUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'oscar',
            email = 'ponte@baquero.com',
            password = 'testpass123'
        )
        
        self.assertEqual(user.username, 'oscar')
        self.assertEqual(user.email, 'ponte@baquero.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'admin',
            email = 'admin@admin.com',
            password = 'testpass123'
        )
        
        self.assertEqual(user.username, 'admin')
        self.assertEqual(user.email, 'admin@admin.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        
        
        
