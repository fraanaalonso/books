from django.contrib.auth import get_user_model #importamos nuestro CustomUserModel a través del setting.py con AUTH_USER_MODEL
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', )