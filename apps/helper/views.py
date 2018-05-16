from django.shortcuts import render, redirect
from .models import Order


#home page shows all the orders that havent shipped out and sort by desc on id(newest objects show 1st)
def index(request):
    context = {
        "order": Order.objects.filter(isShipped = Flase).order_by('-id')
    }
    return render(request, 'helper/index.html', context)


def create(request):
    return True

def newOrderPage(request):
    return True

def managePage(request):
    return True

def delete(request):
    return True

def updateOne(request):
    return True

def showAll(request):
    return True
