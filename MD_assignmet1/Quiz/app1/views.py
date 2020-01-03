from django.shortcuts import render
from .models import AllQuestion
from django.views import View
from django.http import JsonResponse
from .models import QuestionUser
import json
import random
import csv
import os

# with open("C:\\Users\saide\PycharmProjects\MD_assignmet1\Quiz\\app1\python_questions.csv") as cf:
#     reader = csv.reader(cf, delimiter=',')
#     for i in reader:
#         p = AllQuestion(question=i[0], first_choice=i[1], secound_choice=i[2], third_choice=i[3], fourth_choice=i[4],
#                         correct_answer=i[5])
#         p.save()


class QuizView(View):

    def get(self, request, username):
        paper = []
        number_questions = []
        question_id = []
        all_question = AllQuestion.objects.all()
        for k in range(5):
            number_questions.append(random.randint(1, 9))
        for q in all_question:
            if q.id in number_questions:
                paper.append({q.id: {q.question: [q.first_choice, q.secound_choice, q.third_choice, q.fourth_choice]}})
                question_id.append(q.id)
                questions_send = str(question_id)
        questions = QuestionUser(user_id=username, questions_id=questions_send)
        questions.save()
        return JsonResponse(paper, safe=False)

    def post(self, request):
        correct_answer = 0
        wrong_answer = 0
        body = json.loads(request.body.decode('utf-8'))
        for i in body:
            answer = AllQuestion.objects.get(id=int(i))
            if answer.correct_answer == body[i]:
                correct_answer += 1
            else:
                wrong_answer += 1
        soccer = percentage(correct_answer, wrong_answer, 10)
        return JsonResponse({"your soccer is": soccer})


def percentage(correct, wrong, total):
    percent = (((3*correct)-wrong)/(total*3))*100
    return percent
