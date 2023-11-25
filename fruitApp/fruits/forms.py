from django import forms

from fruitApp.fruits.models import Category, Fruit


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class FruitModelForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitDeleteForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'
