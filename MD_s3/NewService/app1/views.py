from django.shortcuts import render
from .models import Users, News
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
import json


class NewsViews(View):
    def get(self, request, year=None, month=None, day=None):
        input_error_flag = False
        news_list = []
        if day is None:
            if month is None:
                if year is None:
                    all_news_write = News.objects.all()
                else:
                    if year != '':
                        all_news_write = News.objects.filter(data_submit_news__year=year)
                    else:
                        input_error_flag = True
            else:
                if year != '' and month != '':
                    all_news_write = News.objects.filter(data_submit_news__year=year, data_submit_news__month=month)
                else:
                    input_error_flag = True
        else:
            if year != '' and month != '' and day != '':
                all_news_write = News.objects.filter(data_submit_news__year=year, data_submit_news__month=month,
                                                     data_submit_news__day=day)
            else:
                input_error_flag = True
        if input_error_flag == False and len(all_news_write) != 0:
            for news in all_news_write:
                news_list.append({news.id: [news.content, news.data_submit_news]})
        elif len(all_news_write) == 0:
            news_list.append({"Result": "Any news is not submit with this condition"})
        elif input_error_flag == True:
            news_list.append({'Input Error': "The type of input is not valid"})
        return JsonResponse(news_list, safe=False)

    def put(self, request, username, id_news):
        author = Users.objects.filter(name=username)
        if author[0].level == 1:
            update_news = News.objects.filter(id=id_news, news_writer=author[0])
            if len(update_news) != 0:
                body = json.loads(request.body.decode('utf-8'))
                update_news[0].content = body['content']
                update_news[0].save()
                return JsonResponse({'Validation': "news with id {} update successfully".format(id_news)})
            else:
                return JsonResponse({"Error": "{} don't have any news with this {}".format(username, id_news)})
        else:
            return JsonResponse({"Error": "{} don\'t hanve permission to update news".format(username)})

    def delete(self, request, username, id_news):
        author = Users.objects.filter(name=username)
        if author[0].level == 1:
            delete_news = News.objects.filter(id=id_news, news_writer=author[0])
            if len(delete_news) != 0:
                delete_news[0].delete()
                return JsonResponse({'Validation': "news with id {} delete successfully".format(id_news)})
            else:
                return JsonResponse({"Error": "{} don't have any news with this {}".format(username, id_news)})
        else:
            return JsonResponse({"Error": "{} don\'t hanve permission to update news".format(username)})

class UserViews(View):

    def post(self, request, username):
        writer_news = Users.objects.filter(name=username)
        if len(writer_news) > 0:
            if writer_news[0].level == 1:
                body = json.loads(request.body.decode("utf-8"))
                news_content = body['content']
                news = News(news_writer=writer_news[0], content=news_content)
                news.save()
                return JsonResponse({'error': 'your news added'})
            else:
                return JsonResponse({'error': '{} don\'t have limitation for submit news'.format(username)})

    def get(self, request, username):
        news_list = []
        writer_news = Users.objects.filter(name=username)
        if len(writer_news) > 0:
            all_news_write = News.objects.filter(news_writer=writer_news[0])
            for news in all_news_write:
                news_list.append({news.id: [news.content, news.data_submit_news]})
            return JsonResponse(news_list, safe=False)
        else:
            return JsonResponse({'Error': "This user in not exist!"})


