from django import forms

from fruitApp.fruits.models import Category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
