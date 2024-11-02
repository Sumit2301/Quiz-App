from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    age = forms.IntegerField(required=False)
    highest_qualification = forms.CharField(max_length=100, required=True)
    preferred_test = forms.ChoiceField(choices=[
        ('test1', 'Test 1'),
        ('test2', 'Test 2'),
        ('test3', 'Test 3'),
    ])

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'age', 'highest_qualification', 'preferred_test')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            # Create UserProfile instance
            profile = UserProfile(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                age=self.cleaned_data['age'],
                highest_qualification=self.cleaned_data['highest_qualification'],
                preferred_test=self.cleaned_data['preferred_test']
            )
            profile.save()
        return user
