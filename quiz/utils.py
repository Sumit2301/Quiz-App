# utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user_email):
    subject = "Welcome to the Quiz Platform"
    message = "Thank you for registering for our quiz platform!"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email, 'sammarvalkar343@gmail.com'])

def send_result_email(user_email, score):
    subject = "Quiz Results"
    message = f"Your quiz is complete! You scored: {score}"
    send_mail(subject, message, settings.EMAIL_HOST_USER, [user_email, 'sammarvalkar343@gmail.com'])
