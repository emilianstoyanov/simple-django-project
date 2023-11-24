from django.core.exceptions import ValidationError


def only_alphabet(value):
    if any(i.isalpha() for i in value):
        raise ValidationError("Fruit name should contain only letters!")
