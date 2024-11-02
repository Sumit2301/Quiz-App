# quiz/urls.py

from django.urls import path
from .views import (
    register,
    login_view,
    quiz_selection,
    take_quiz,
    quiz_results,
    password_reset,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('quiz_selection/', quiz_selection, name='quiz_selection'),
    path('take_quiz/', take_quiz, name='take_quiz'),  # This line defines the URL for the take_quiz view
    path('quiz_results/<int:score>/<int:total>/', quiz_results, name='quiz_results'),
    path('password_reset/', password_reset, name='password_reset'),
]
