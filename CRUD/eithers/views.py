from django.shortcuts import render, redirect
from .models import Question, Answer
from random import choice


# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'eithers/index.html', context)


def new(request):
    if request.method == 'POST':
        question = Question()
        question.title = request.POST.get('title') 
        question.issue_a = request.POST.get('issue_a') or 'agree'
        question.image_a = request.FILES.get('image_a')
        question.issue_b = request.POST.get('issue_b') or 'disagree'
        question.image_b = request.FILES.get('image_b')
        question.save()
        return redirect('home')
    else:
        return render(request, 'eithers/new.html')


def detail(request, pk):
    question = Question.objects.get(id=pk)
    answers = question.answer_set.all()
    all_num = question.answer_set.count()
    a = question.answer_set.filter(pick=1).count()
    b = question.answer_set.filter(pick=0).count()
    context = {
        'question': question,
        'answers': answers,
        'agree': a,
        'agree_rate': all_num and '{:0.2f}'.format(100 * a/all_num),
        'disagree': b,
        'disagree_rate': all_num and '{:0.2f}'.format(100 * b/all_num),
    }
    return render(request, 'eithers/detail.html', context)

def answers_create(request, pk, pick):
    question = Question.objects.get(id=pk)
    answer = Answer()
    answer.question = question
    answer.pick = pick
    answer.save()

    return redirect('eithers:detail', question.id)

def detail_answer(request, pk):
    answer = Answer.objects.get(id=pk)
    question = answer.question
    context = {
        'question': question,
        'answer': answer,
        'agree': a,
        'disagree': b
    }
    return render(request, 'eithers/detail_answer.html', context)

def answers_delete(request, pk):
    answer = Answer.objects.get(id=pk)
    answer.delete()
    return redirect('eihers:index')

def random(request):
    questions = Question.objects.all()
    question = choice(questions)
    
    return redirect('eithers:detail', question.id)

# def detail(request, pk):
#     question = Question.objects.get(id=pk)
#     answers = question.answer_set.all()
#     context = {
#         'question' = question,
#         'answers' = answers,
#     }
#     return render(request, 'detail.html', context)

