from pyexpat import model
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label=_('email'),
        max_length=255,
        widget=forms.EmailInput(attrs={'autocomplete':'emil'})
    )
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class meta(UserCreationForm.Meta):
        model = User
        fields = ('__all__')






   