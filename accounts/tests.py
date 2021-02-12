from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve
from .forms import CustomUserCreationForm
from .views import SingupPageView
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
        
    
        
class SignupTestCase(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
        
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! Fuck You!!!')      
        
        
    #testing our custom creation form is being used
    
    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')
        
    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(
            view.func.__name__,
            SingupPageView.as_view().__name__
        )
        
        
