#from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    context = {
        'text': 'This is my text',
        'question': 'This is my question',
        'answer': 'This is my answer',
        'list_of_titles': ['1984', 'Joker', 'Youtube', 'Bits', 22],
        'phrase': 'Never come back, never say "hi"',
    }
    return render(request, 'home.html', context)
