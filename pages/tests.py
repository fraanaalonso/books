from django.test import SimpleTestCase
from django.urls import resolve, reverse #useful for testing URLs
from .views import HomePageView

class HomePageTest(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.resp = self.client.get(url)
        
    def test_homepage_status_code(self):
        self.assertEqual(self.resp.status_code, 200)
        
    def test_homepage_template(self):
        self.assertTemplateUsed(self.resp, 'home.html')
        
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.resp, 'Home')
        
    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.resp, 'Hi there! Fuck you.')
        
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )