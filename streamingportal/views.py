from django.shortcuts import render
from django.http.response import HttpResponse


def browse(request):
    return HttpResponse("Hello")