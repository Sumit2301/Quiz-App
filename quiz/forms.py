from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Question, UserProfile
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    age = forms.IntegerField(required=False)
    highest_qualification = forms.CharField(max_length=100, required=True)
    preferred_test = forms.ChoiceField(choices=[
        ('test1', 'Test 1'),
        ('test2', 'Test 2'),
        ('test3', 'Test 3'),
    ])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'age', 'highest_qualification', 'preferred_test')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                highest_qualification=self.cleaned_data['highest_qualification'],
                preferred_test=self.cleaned_data['preferred_test']
            )
        return user

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'option1', 'option2', 'option3', 'option4', 'correct_option']
