from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('quiz_selection/', views.quiz_selection, name='quiz_selection'),
    path('take_quiz/', views.take_quiz, name='take_quiz'),
    path('quiz_results/<int:score>/<int:total>/', views.quiz_results, name='quiz_results'),
    path('questions/', views.question_list, name='question_list'),
    path('questions/create/', views.create_question, name='create_question'),
    path('questions/update/<int:pk>/', views.update_question, name='update_question'),
    path('questions/delete/<int:pk>/', views.delete_question, name='delete_question'),
]
