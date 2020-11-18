from django.shortcuts import render, redirect
from store.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def store(request):
     context = {}
     return render(request, 'store/store.html', context)

def cart(request):
     context = {}
     return render(request, 'store/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'store/checkout.html', context)

"""def login(request):
      context = {}
      return render(request, 'store/login.html', context)"""

def loginSingup(request):
     if request.method=="POST":
          if request.POST.get('loginEmail'):
               username = request.POST.get('loginEmail')
               password = request.POST.get('loginPassword')
               try:
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    messages.info(request, "Bienvenido!!!")
                    return render(request, 'store/login.html')
               except:
                    messages.info(request, "No existe el usuario!!!")
          else:
               if request.POST.get('singupPassword') == request.POST.get('singup2Password'):
                    username = request.POST.get('singupEmail')
                    password = request.POST.get('singupPassword')
                    user = User.objects.create_user(username, username, password)
                    user.save()
                    if request.POST.get('singupShareCode'):
                         customer = Customer(user=user, name=username, email=username, password=password, isPrimary=False, familyCode=request.POST.get('singupShareCode'))
                         customer.save()
                    else:
                         customer = Customer(user=user, name=username, email=username, password=password, isPrimary=True, familyCode='Código Ejemplo')
                         customer.save()
                    login(request, user)
                    messages.info(request, "Registro exitoso!!!")
                    return redirect('store')
               else:
                    messages.info(request, "Las contraseñas no coinciden!!!")
     else:
          return render(request, 'store/login.html')