from django.shortcuts import render
from .models import Menu, MenuGroups

# Create your views here.
def index(request):
    # hide_header = False

    # if request.method == 'GET' and request.GET.get('scroll') == 'up':
    #     hide_header = True
    

    context = {#'hide_header': hide_header,
               'fade_out': True,
               'current_page': 'home',
               }
    
    return render(request, "main/index.html", context)

def menu(request):
    # hide_header = False

    # if request.method == 'GET' and request.GET.get('scroll') == 'up':
    #     hide_header = True
    menu_groups = MenuGroups.objects.order_by("id")
    menu = Menu.objects.order_by("id")
    
    context = {#'hide_header': hide_header,
               'fade_out': True,
               'current_page': 'menu',
               'menu': menu,
               'menu_groups': menu_groups,
            }
    
    return render(request, "main/menu.html", context)

def contacts(request):
    # hide_header = False

    # if request.method == 'GET' and request.GET.get('scroll') == 'up':
    #     hide_header = True

    context = {#'hide_header': hide_header,
               'fade_out': True,
               'current_page': 'contact'}

    return render(request, "main/contacts.html", context)

def delivery(request):
    # hide_header = False

    # if request.method == 'GET' and request.GET.get('scroll') == 'up':
    #     hide_header = True
    

    context = {#'hide_header': hide_header,
               'fade_out': True,
               'current_page': 'delivery',
               }
    
    return render(request, "main/delivery.html", context)

def about_us(request):
    hide_header = False

    if request.method == 'GET' and request.GET.get('scroll') == 'up':
        hide_header = True
    

    context = {'hide_header': hide_header,
               'fade_out': True,
               'current_page': 'about-us',
               }
    
    return render(request, "main/about-us.html", context)
