from django.shortcuts import render

from fruitApp.fruits.models import Fruit


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits,
    }
    return render(request, 'common/dashboard.html', context)


def create_fruit(request):
    return render(request, 'fruits/create-fruit.html')


def detail_fruit(request, fruit_pk):
    fruit = Fruit.object.get(pk=fruit_pk)
    context = {'fruit': fruit}
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_pk):
    return render(request, 'fruits/edit-fruit.html')


def delete_fruit(request, fruit_pk):
    return render(request, 'fruits/delete-fruit.html')


def create_category(request):
    return render(request, 'categories/create-category.html')
