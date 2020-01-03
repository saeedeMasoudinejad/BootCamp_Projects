from django.shortcuts import render
from .models import Questions
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def fetch_question_ravan(request):
    select_questions = {}
    if request.method == 'GET':
        all_questions = Questions.objects.filter(category='ravanshenasi')
        for i in all_questions:
            select_questions[i.id] = i.content
    return JsonResponse(select_questions)


def fetch_question_varzesh(request):
    select_questions = {}
    if request.method == 'GET':
        all_questions = Questions.objects.filter(category='varzeshi')
        for i in all_questions:
            select_questions[i.id] = i.content
    return JsonResponse(select_questions)


def fetch_question_eghtesad(request):
    select_questions = {}
    if request.method == 'GET':
        all_questions = Questions.objects.filter(category='eghtesad')
        for i in all_questions:
            select_questions[i.id] = i.content
    return JsonResponse(select_questions)