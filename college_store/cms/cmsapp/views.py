from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonCreationForm
from .models import Person, Course


# Create your views here.
def home(request):
    return render(request, 'home.html')

def details(request):
    return render(request, 'details.html')



def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request, 'details.html', {'user': user})
            else:
                messages.info(request, 'Invalid credentials')
                return redirect('cmsapp:login')
        else:
            return render(request, 'login.html')
    else:
        return redirect('cmsapp:person_add')


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['password1']

            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username already exists')
                    return redirect('cmsapp:register')

                else:
                    user = User.objects.create_user(username=username,
                                                    password=password,

                                                    )
                    user.save()
                    print("user created")
                    return redirect('cmsapp:login')
            else:
                print("passwords not matching")
                messages.info(request, 'passwords not matching')
                return redirect('cmsapp:register')
        else:
            return render(request, 'register.html')
    else:
        return redirect('cmsapp:person_add')


def details_form(request):
    return render(request, 'details_form.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def person_create_view(request):
    if request.user.is_authenticated:
        form = PersonCreationForm()
        if request.method == 'POST':

            form = PersonCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, "Details added successfully")
                return redirect('cmsapp:person_add')
        return render(request, 'index.html', {'form': form})
    else:
        return redirect('cmsapp:login')


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'index.html', {'form': form})


# AJAX
def load_cities(request):
    print("hellooooo")
    department_id = request.GET.get('department_id')

    cities = Course.objects.filter(department_id=department_id).all()
    print(cities)
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
