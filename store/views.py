from django.shortcuts import render, redirect
from store.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as django_logout
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
     if not request.user.is_authenticated:
          if request.method=="POST":
               if request.POST.get('loginEmail'):
                    username = request.POST.get('loginEmail')
                    password = request.POST.get('loginPassword')
                    user = authenticate(username=username, password=password)
                    if user is not None:
                         login(request, user)
                         messages.info(request, "Bienvenido!!!")
                         return redirect('store')
                    else:
                         messages.info(request, "Usuario y/o contraseña incorrecta(s)!!!")
                         return render(request, 'store/login.html')
               else:
                    if request.POST.get('singupPassword') == request.POST.get('singup2Password'):
                         username = request.POST.get('singupEmail')
                         password = request.POST.get('singupPassword')
                         q1 = User.objects.filter(username=username)
                         if request.POST.get('singupShareCode'):
                              q2 = Customer.objects.filter(familyCode=request.POST.get('singupShareCode'))
                              if not q2:
                                   messages.info(request, "El código compartido que ingresaste no existe!!!")
                                   return render(request, 'store/login.html')
                              else:
                                   if not q1:
                                        user = User.objects.create_user(username, username, password)
                                        user.save()
                                   else:
                                        messages.info(request, "El e-mail ya está registrado!!!")
                                        return render(request, 'store/login.html')
                                   customer = Customer(user=user, name=username, email=username, password=password, isPrimary=False, familyCode=request.POST.get('singupShareCode'))
                                   customer.save()
                         else:
                              if not q1:
                                   user = User.objects.create_user(username, username, password)
                                   user.save()
                              else:
                                   messages.info(request, "El e-mail ya está registrado!!!")
                                   return render(request, 'store/login.html')
                              customer = Customer(user=user, name=username, email=username, password=password, isPrimary=True, familyCode='codigoEjemplo')
                              customer.save()
                         login(request, user)
                         if customer.isPrimary:
                              messages.info(request, "¡Registro exitoso! | TU CÓDIGO COMPARTIDO ES: codigoEjemplo")
                         else:
                              messages.info(request, "¡Registro exitoso!")
                         return redirect('store')
                    else:
                         messages.info(request, "Las contraseñas no coinciden!!!")
                         return render(request, 'store/login.html')
          else:
               return render(request, 'store/login.html')
     else:
          messages.info(request, "Ya iniciaste sesión!!!")
          return redirect('store')

def logout(request):
     django_logout(request)
     messages.info(request, "Sesión terminada!!!")
     return redirect('store')