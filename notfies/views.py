from django.shortcuts import render
from django.http import HttpResponse
from .models import Lists
def index(request):
    all_lists = Lists.objects.all()
    html = ' '
    for list in all_lists:
        url = '/notfies/' + str(lists.id) + '/'
        html += ' <a href="'+ url +'">' + list.tasks + '</a> <br>'
    return HttpResponse(html)
def detail(request,lists):
    return HttpResponse("<h2>Who is on the list "+str(lists)+ "</h2>")
# Create your views here.
