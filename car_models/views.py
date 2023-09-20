from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def index(request):
    forma = Car_()
    bd = Car.objects.all()
    data = {'forma':forma, 'database':bd}
    return render(request, 'index.html', context=data)

def create(request):  # функция для создания объекта со страницы html
    if request.POST:  # проверка если в поля введены данные то присваиваем эти данные в переменные
        car = Car()  # создание объекта на основе класса
        car.stamp = request.POST.get('stamp_')
        car.manufacturer = request.POST.get('manufacturer_')
        car.release_date = request.POST.get('release_date_')
        car.state_number = request.POST.get('state_number_')
        car.save() # метод сохранения в страницу
        return redirect('home') # возврат адресом home

        # data = {'stamp': stamp,
        #         'manufacturer': manufacturer,
        #         'release_date': release_date,
        #         'state_number': state_number,
        #         }
        # return render(request, 'out.html', context=data)

def delete(request, ids):
    car = Car.objects.get(id=ids) # заходим в таблицу и забираем одного
    car.delete()  # метод удаления
    return redirect('home') # возврат адресом home