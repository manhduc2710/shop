from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from .form import *
from django.contrib.auth.decorators import login_required

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
    obj = carousel.objects.all()
    context = {'products': products, 'categories': categories, 'cartItem': cartItem, 'page': page, 'obj': obj}
    return render(request, 'pages/home.html', context)
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        cartItem = order.get_cart_items
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItem = order['get_cart_items']
    id = request.GET.get('id', '')
    product = Product.objects.filter(id=id)
    products = Product.objects.all()
    categories = Category.objects.filter(is_sub=False)
    page = Paginator(products, 4)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    context = {'product': product, 'products': products, 'categories': categories, 'page': page, 'cartItem': cartItem}
    return render(request, 'pages/detail.html', context)
def cart(request):
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
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = { 'items': items, 'order': order, 'categories': categories, 'cartItem': cartItem}
    return render(request, 'pages/cart.html', context)
def checkout(request):
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
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
    context = { 'items': items, 'order': order, 'categories': categories, 'cartItem': cartItem}
    return render(request, 'pages/checkout.html', context)
def loginpage(request):
    categories = Category.objects.filter(is_sub=False)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        cartItem = order.get_cart_items
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItem = order['get_cart_items']
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

    context = {'cartItem': cartItem, 'categories': categories}
    return render(request, 'pages/login.html', context)
def logout(request):
    logout(request)
    return redirect('login')
def register(request):
    categories = Category.objects.filter(is_sub=False)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        cartItem = order.get_cart_items
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItem = order['get_cart_items']
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form, 'cartItem': cartItem, 'categories': categories}
    return render(request, 'pages/register.html', context)
def search(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        cartItem = order.get_cart_items
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItem = order['get_cart_items']
    if request.method == "POST":
        searched = request.POST.get('searched')
        keys = Product.objects.filter(name__contains=searched)
    categories = Category.objects.filter(is_sub=False)
    context = {'searched': searched, 'keys': keys, 'categories': categories, 'cartItem': cartItem}
    return render(request, 'pages/search.html', context)
def category(request):
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
    active_category = request.GET.get('category','')

    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    context = {'categories': categories, 'products': products, 'active_category': active_category, 'cartItem': cartItem}
    return render(request, 'pages/category.html', context)
def updateItem(request):
    data = JsonResponse.loads(request.body)
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

@login_required(login_url={'login'})
def wishlist(request):
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
    wishlist = Favorites.objects.filter(customer = request.user)
    context = {'wishlist': wishlist, 'categories': categories, 'cartItem': cartItem}
    return render(request, 'pages/wishlist.html', context)

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('productId'))
            product = Product.objects.get(id=prod_id)
            if(product):
                if(Order.objects.filter(customer=request.user.id, productId=prod_id)):
                    return JsonResponse({'status': "Product Already in Cart"})  
                else:
                    prod_qty = int(request.POST.get('productQty'))
                    if product.quantity >= prod_qty:
                        Order.objects.create(customer = request.user, productId = prod_id, productQty = prod_qty)
                        return JsonResponse({'status': "Product added Successfully"})  
                    else:
                        return JsonResponse({'status': "Only " + str(product.quantity)+ " quantity available"}) 
            else:
                return JsonResponse({'status': "No such product found"})    
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')