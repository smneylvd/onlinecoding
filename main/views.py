from django.shortcuts import render

# Create your views here.

def index(req) :
    return render(req, 'onlineCoding/index.html')


def demo(req):
    return render(req, 'onlineCoding/demo.html')


def authPage(req):
    return render(req, 'onlineCoding/authorization.html')


def editorPage(req):
    return render(req, 'onlineCoding/textEditor.html')