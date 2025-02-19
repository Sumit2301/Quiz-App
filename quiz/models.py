from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()

    def __str__(self):
        return self.question_text

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    highest_qualification = models.CharField(max_length=100, null=True, blank=True)
    preferred_test = models.CharField(
        max_length=20,
        choices=[('test1', 'Test 1'), ('test2', 'Test 2'), ('test3', 'Test 3')],
        default='test1',
    )

    def __str__(self):
        return self.user.username
