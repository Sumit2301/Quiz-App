from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, QuestionForm
from .models import Question
from django.core.mail import send_mail

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'quiz/register.html', {'form': form})

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

@login_required
def quiz_selection(request):
    return render(request, 'quiz/quiz_selection.html')

@login_required
def take_quiz(request):
    questions = Question.objects.all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer = request.POST.get(str(question.id))
            if selected_answer and int(selected_answer) == question.correct_option:
                score += 1
        send_mail(
            'Quiz Results',
            f'You scored {score} out of {len(questions)}.',
            'your_email@example.com',
            [request.user.email],
        )
        return redirect('quiz_results', score=score, total=len(questions))
    return render(request, 'quiz/take_quiz.html', {'questions': questions})

@login_required
def quiz_results(request, score, total):
    return render(request, 'quiz/quiz_results.html', {'score': score, 'total': total})

@login_required
def question_list(request):
    questions = Question.objects.all()
    return render(request, 'quiz/question_list.html', {'questions': questions})

@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question created successfully!')
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'quiz/question_form.html', {'form': form})

@login_required
def update_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question updated successfully!')
            return redirect('question_list')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'quiz/question_form.html', {'form': form})

@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Question deleted successfully!')
        return redirect('question_list')
    return render(request, 'quiz/question_confirm_delete.html', {'question': question})
