from django.test import SimpleTestCase
from django.urls import resolve, reverse #useful for testing URLs
from .views import HomePageView, AboutPageView

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


class AboutPageTest(SimpleTestCase):
    def setUp(self):
        url = reverse('about') #get the URL
        self.response = self.client.get(url)
    
    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_contains_correct_html(self):
        self.assertTemplateUsed(self.response, 'about.html')
    
    def test_aboutpage_does_not_contains_correct_html(self):
        self.assertNotContains(
            self.response, 'hi there! Fuck you'
        )

    def test_aboutpage_resolve_url_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )