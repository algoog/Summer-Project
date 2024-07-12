from django.shortcuts import render, redirect
from .models import Person, House
from .forms import PersonForm, HouseForm

def index(request):
    return render(request, 'mysite/index.html')

def people_list(request):
    people = Person.objects.all()
    return render(request, 'mysite/people_list.html', {'people': people})

def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people_list')
    else:
        form = PersonForm()
    return render(request, 'mysite/add_person.html', {'form': form})

def add_house(request):
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('people_list')
    else:
        form = HouseForm()
    return render(request, 'mysite/add_house.html', {'form': form})