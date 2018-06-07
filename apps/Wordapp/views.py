from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index (request):
    RandomWord = get_random_string(length=32)
    contex = {
        'word':RandomWord
    }
    return render(request, 'Wordapp/index.html',contex) 