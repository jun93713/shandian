from django.shortcuts import render, redirect
from .models import Order
from django.db.models import Q


#home page shows all the orders that havent shipped out and sort by desc on id(newest objects show 1st)
def index(request):
    context = {
        "orders": Order.objects.filter(isArrived=False).order_by('-id')
    }
    return render(request, 'helper/index.html', context)

#create new order into db
def create(request):
    if request.method == "POST":
        Order.objects.create(request.POST)
    return redirect('/')

#render page to create new order
def newOrderPage(request):
    return render(request, 'helper/newOrderPage.html')

#render page display info for single order and able to modify status
def managePage(request, id):
    context = {
        "order": Order.objects.get(id = id)
    }
    return render(request, 'helper/managePage.html', context)

#remove single order, rarely use
def remove(request, id):
    if request.method == "POST":
        Order.objects.get(id = id).delete()
    return redirect('/')

#update single order status
def updateOne(request, id):
    if request.method == "POST":
        Order.objects.update(request.POST, id)
    return redirect('/')

#render a page to display all shipped orders
def showAll(request):
    context = {
        "orders": Order.objects.filter(isArrived = True).order_by('-id')
    }
    return render(request, 'helper/showAllPage.html', context)

#search name or item
def search(request):

    if request.method == "POST":
        word = request.POST['words']
        context = {
            "orders": Order.objects.filter(
                Q(name__contains = word) | Q(item__contains = word),
                Q(isArrived = False)
            )
        }

    else:
        context = {
            "error": "can't find anything"
        }

    return render(request, 'helper/searchPage.html', context)

def plist(request):
    context = {
        "orders": Order.objects.filter(isPurchased = False).order_by('id')
    }
    return render(request, 'helper/notPurchased.html', context)

def slist(request):
    context = {
        "orders": Order.objects.filter(isShipped = False).order_by('id')
    }
    return render(request, 'helper/notShipped.html', context)

def about(request):
    return render(request, 'helper/about.html')

def groupPurchase(request):
    if request.method == "POST":
        ids = []
        for key in request.POST:
            ids.append(key)
        for id in ids[1:]:
            order = Order.objects.get(id=id)
            order.isPurchased = True
            order.save()
    return redirect('/purchaselist')

def groupShip(request):
    if request.method == "POST":
        ids = []
        for key in request.POST:
            ids.append(key)
        for id in ids[1:]:
            order = Order.objects.get(id=id)
            order.isShipped = True
            order.save()
    return redirect('/shoplist')

def groupDelete(request):
    if request.method == "POST":
        ids = []
        for key in request.POST:
            ids.append(key)
        for id in ids[1:]:
            Order.objects.get(id=id).delete()
    return redirect('/shoplist')
