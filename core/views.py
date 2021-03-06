from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Question, Answer, search_questions_for_user, get_question_for_user
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Count, Min, Q


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('list_questions')
    return render(request, 'core/home.html')


@login_required
def list_questions(request):
    questions = request.user.questions.all()
    return render(request, 'core/list_questions.html', {'questions': questions})


@login_required
def show_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    form = QuestionForm()
    answers = question.answers.order_by('created')
    user_favorite = request.user.is_favorite_question(question)
    return render(request, 'core/show_question.html', {'question': question, 'pk': pk, 'form': form, 'answers': answers, 'user_favorite': user_favorite})


@login_required
def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect(to='list_questions')
    else:
        form = QuestionForm()
    return render(request, 'core/add_question.html', {'form': form})


@login_required
def add_answer(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)

    if request.method == 'POST':
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.instance
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect(to='show_question', pk=pk)
    else:
        form = AnswerForm()

    return render(request, 'core/add_answer.html', {'form': form, 'question': question})


@login_required
def edit_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    if request.method == 'POST':
        form = QuestionForm(data=request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return redirect(to='list_questions')
    else:
        form = QuestionForm(instance=question)
    
    return render(request, 'core/edit_question.html', {'form': form, 'question': question})


@login_required
def delete_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Question deleted.')
        return redirect(to='list_questions')
    
    return render(request, 'core/delete_question.html', {'question': question})


@login_required
@csrf_exempt
@require_POST
def favorite_question(request, pk):
    question = get_object_or_404(request.user.questions, pk=pk)
    if question in request.user.favorite_question.all():
        request.user.favorite_question.remove(question)
        return JsonResponse({'favorite': False})
    else:
        request.user.favorite_question.add(question)
        return JsonResponse({'favorite': True})


def search_questions(request):
    query = request.GET.get('q')
    if query is not None:
        questions = Question.objects.search(query).for_user(request.user).public()
    else:
        questions = None
    
    return render(request, 'core/search.html', {'questions': questions, 'query': query or ""})