from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Question
from django.core.mail import send_mail

# User registration
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'quiz/register.html', {'form': form})

# User login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quiz_selection')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'quiz/login.html')

# Quiz selection view
@login_required
def quiz_selection(request):
    return render(request, 'quiz/quiz_selection.html')

# Take quiz view
@login_required
def take_quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer = request.POST.get(str(question.id))
            if selected_answer and int(selected_answer) == question.correct_option:
                score += 1
        # Send email with the score
        send_mail(
            'Your Quiz Results',
            f'You scored {score} out of {len(questions)}.',
            'your_email@gmail.com',  # Replace with your email
            [request.user.email],
            fail_silently=False,
        )
        return redirect('quiz_results', score=score, total=len(questions))

    return render(request, 'quiz/take_quiz.html', {'questions': questions})

# Quiz results view
@login_required
def quiz_results(request, score, total):
    return render(request, 'quiz/quiz_results.html', {'score': score, 'total': total})

# Password reset view
def password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']
        messages.success(request, 'Password reset link has been sent to your email.')
        return redirect('login')
    return render(request, 'quiz/password_reset.html')
