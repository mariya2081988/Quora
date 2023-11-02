
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quora:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('quora:view_question')
    return render(request, 'login.html')

@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('quora:view_question')
    else:
        form = QuestionForm()
    return render(request, 'post_question.html', {'form': form})

def view_question(request):

    questions = Question.objects.all()
    return render(request, 'view_question.html', {'questions': questions})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(id=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('quora:view_question')
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'form': form, 'question': question})

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get( id=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)

    if not created:
        like.delete()
    return redirect('quora:view_question')


@login_required
def user_logout(request):
    logout(request)
    return redirect('quora:login')
