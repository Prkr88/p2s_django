from django.shortcuts import render
from main_app.forms import UserForm
from main_app.models import Item,Ship,Ship_Type

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

logged_in = False

# Create your views here.
def index(request):
    print(logged_in)
    if logged_in:
        return render(request, 'main_app/index.html')
    else:
        form = UserForm()
        return render(request, 'main_app/login.html', {'form': form})

@login_required
def user_logout(request):
    global logged_in
    # Log out the user.
    logout(request)
    logged_in = False
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    global logged_in
    form = UserForm()
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
        # If we have a user
        if user:
            # Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request, user)
                # Send the user back to some page.
                # In this case their homepage.
                logged_in = True
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'main_app/login.html', {'form':form})


def order_parts(request):
    part_list = Item.objects.order_by('item_name')
    part_dict = {"part_list": part_list}
    return render(request, 'main_app/order_parts.html',part_dict)


def fleet_status(request):
    ships = Ship.objects.all()
    type_list = {}
    for ship in ships:
        type_list[ship.type] = {}
    for ship in ships:
        type_list[ship.type][ship] = {'status': ship.status, 'ship_nm:': ship.n_m}
    type_dict = {"type_list": type_list}
    return render(request, 'main_app/fleet_status.html',type_dict)


def select_section(request):
    return render(request, 'main_app/select_section.html')