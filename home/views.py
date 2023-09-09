from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from .form import *

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        cartItem = order.get_cart_items
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItem = order['get_cart_items']
    categories = Category.objects.filter(is_sub=False)
    products = Product.objects.all()    
    page = Paginator(products, 8)
    page_list = request.GET.get("page")
    page = page.get_page(page_list) 
    context = {'products': products, 'categories': categories, 'cartItem': cartItem, 'page': page}
    return render(request, 'pages/home.html', context)
def detail(request):
    id = request.GET.get('id', '')
    product = Product.objects.filter(id=id)
    products = Product.objects.all()
    categories = Category.objects.filter(is_sub=False)
    context = {'product': product, 'products': products, 'categories': categories}
    return render(request, 'pages/detail.html', context)
def card(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = { 'items': items, 'order': order}
    return render(request, 'pages/card.html', context)
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = { 'items': items, 'order': order}
    return render(request, 'pages/checkout.html', context)
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: messages.info(request, 'user or password not correct!')

    context = {}
    return render(request, 'pages/login.html', context)
def logout(request):
    logout(request)
    return redirect('login')
def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'pages/register.html', context)
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        keys = Product.objects.filter(name__contains=searched)
    categories = Category.objects.filter(is_sub=False)
    context = {'searched': searched, 'keys': keys, 'categories': categories}
    return render(request, 'pages/search.html', context)
def category(request):
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category','')

    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    context = {'categories': categories, 'products': products, 'active_category': active_category}
    return render(request, 'pages/category.html', context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id =productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    elif orderItem.quantity <= 0:
        orderItem.delete()
    orderItem.save()


    return JsonResponse('add', safe=False)

def wishlist(request):
    if request.user.is_authenticated:
        customer = request.user
        favorites, created = Favorites.objects.get_or_create(customer = customer, complete = False)
    categories = Category.objects.filter(is_sub=False)
    context = {'favorites': favorites, 'categories': categories}
    return render(request, 'pages/wishlist.html', context)