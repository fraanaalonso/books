from django.urls import path
from .views import SingupPageView

urlpatterns = [
    path('signup/', SingupPageView.as_view(), name="signup"),
]
