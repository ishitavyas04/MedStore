from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import Product
from .models import Productview
from .models import Catergory
from .models import Customer
from .models import Order
from django.contrib.auth.hashers import make_password , check_password
# Create your views here.


def home(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        prds = Product.get_all_products()
        print('you are :' ,request.session.get('email'))
        return render(request, "home.html", {'products': prds})


    else:
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:    
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1    
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print( request.session['cart'] )
        return redirect('home')




def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")

    else:
        postData = request.POST
        username = postData.get('username')
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        mobno = postData.get('mobno')
        email = postData.get('email')
        age = postData.get('age')
        password = postData.get('password')
        confirmpassword = postData.get('confirmpassword')
        city = postData.get('city')
        address = postData.get('address')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'mobno': mobno,
            'email': email,
            'age': age,
            'city': city,
            'address': address,

        }
        # validation
        customer = Customer(username=username, first_name=first_name, last_name=last_name, email=email,
                        mobno=mobno, age=age, password=password, confirmpassword=confirmpassword, city=city, address=address)

        error_message = None
        if (not first_name):
            error_message = "First Name Required!"
        elif len(first_name) < 4:
            error_message = 'First Name must be 4 character or More'
        elif not last_name:
            error_message = 'Last Name Required!'
        elif len(last_name) < 4:
            error_message = 'Last Name must be 4 char long or more '
        elif not mobno:
            error_message = 'Phone Number required'
        elif len(mobno) < 10:
            error_message = 'Phone Number must be 10 digit'
        elif not age:
            error_message = 'age is required'

        elif not password:
            error_message = 'Password is Required'
        elif len(password) < 6:
            error_message = 'password must contain 6 letter'
        elif not confirmpassword:
            error_message = ' Confirm Password is Required'
        elif not password == confirmpassword:
            error_message = 'Password Not Matched'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'    

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)


def login(request):
    if request.method == 'GET':
        return render(request , 'login.html')
    else:    
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password ,customer.password)
            if flag:
                request.session['customer'] = customer.id
                return redirect('/')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')

def view(request):
    proview = Productview.get_all_productviews()
    return render(request, "view.html", {'productviews': proview})


def diabetic(request):
    return render(request, "diabetic.html")


def malaria(request):
    return render(request, "malaria.html")


def cancer(request):
    return render(request, "cancer.html")


def thyroid(request):
    return render(request, "thyroid.html")


def typhoid(request):
    return render(request, "typhoid.html")


def cart(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    print(products)
    return render(request , 'cart.html' , {'products' : products} )

def CheckOut(request):    
    if request.method == 'POST':    
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))

            order.save()              
        
        request.session['cart'] = {}
        
        return redirect('cart')    

def OrderView(request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request , 'order.html'  , {'orders' : orders})
