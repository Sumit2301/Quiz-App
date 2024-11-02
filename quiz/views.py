from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Question
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse  # Importing reverse function

# User registration
def register(request):
    """Handle user registration."""
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
    """Handle user login."""
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
    """Render quiz selection page for logged-in users."""    
    return render(request, 'quiz/quiz_selection.html')

# Take quiz view
@login_required
def take_quiz(request):
    questions = Question.objects.all()
    total_questions = questions.count()
    question_number = int(request.GET.get('q', 0))  # Get the current question index

    if question_number < 0 or question_number >= total_questions:
        return redirect('quiz_results', score=0, total=total_questions)

    current_question = questions[question_number] if questions else None

    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        score = int(request.POST.get('score', 0))

        if selected_answer and int(selected_answer) == current_question.correct_option:
            score += 1

        if question_number < total_questions - 1:
            return redirect(reverse('take_quiz') + f'?q={question_number + 1}&score={score}')
        else:
            return redirect('quiz_results', score=score, total=total_questions)

    return render(request, 'quiz/take_quiz.html', {
        'question': current_question,
        'question_number': question_number,
        'total_questions': total_questions,
    })

# Quiz results view
@login_required
def quiz_results(request, score, total):
    """Display the results of the quiz taken."""    
    # Send email with the score
    send_mail(
        'Your Quiz Results',
        f'You scored {score} out of {total}.',
        settings.EMAIL_HOST_USER,  # Your email
        [request.user.email],
        fail_silently=False,
    )
    return render(request, 'quiz/quiz_results.html', {'score': score, 'total': total})

# Password reset view
def password_reset(request):
    """Handle password reset request."""
    if request.method == 'POST':
        email = request.POST['email']
        # Here you would include logic to handle sending a password reset email.
        messages.success(request, 'Password reset link has been sent to your email.')
        return redirect('login')
    return render(request, 'quiz/password_reset.html')
