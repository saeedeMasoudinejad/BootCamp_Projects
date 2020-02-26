from django.shortcuts import render
from .models import Book, Writer
from django.views import View
from django.http import JsonResponse


class Show_book(View):
    def get(self, request):
        all_book = Book.objects.all()
        book_list = []
        for i in all_book:
            writer = i.wirter.all()
            writer_list = []
            for j in writer:
                writer_list.append(j.name)
            book_list.append({i.name: writer_list})
        return JsonResponse(book_list, safe=False)


class Show_writer(View):
    def get(self, request):
        all_writer = Writer.objects.all()
        writer_list = []
        for i in all_writer:
            # book = i.book_set.all() # id don't user related name can use _set as delfult
            # book = i.books.all()   #use related name
            book = i.book.filter(name='b1')
            book_list = []
            for j in book:
                book_list.append(j.name)
            writer_list.append({i.name: book_list})
        return JsonResponse(writer_list, safe=False)