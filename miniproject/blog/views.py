from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<div><h1>Hello World</h1>'
                        '<h2>HEEEEEEEEEE</h2>'
                        '<button> buls </button>'
                        '</div>')


def test(request):
    return HttpResponse('<div><h1>Hello World</h1>'
                        '<h2>HEEEEEEEEEE</h2>'
                        '<button> buls </button>'
                        '</div>')

# Create your views here.
