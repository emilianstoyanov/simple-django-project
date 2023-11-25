from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from fruitApp.fruits.forms import CategoryModelForm, FruitModelForm, FruitDeleteForm
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
    # fruit = Fruit.object.get(pk=fruit_pk)
    fruit = get_object_or_404(Fruit, pk=fruit_pk)
    context = {'fruit': fruit}
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_pk):
    fruit = get_object_or_404(Fruit, pk=fruit_pk)

    if request.method == 'POST':
        form = FruitModelForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
    else:
        form = FruitModelForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_pk):
    fruit = Fruit.objects.filter(pk=fruit_pk).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)

        if form.is_valid():
            fruit.delete()

            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', context)


def create_category(request):
    if request.method == 'POST':
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('create-category')
    else:
        form = CategoryModelForm()

    context = {
        'form': form
    }
    return render(request, 'categories/create-category.html', context)


class FruitFormView(FormView):
    form_class = FruitModelForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('create-category')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
