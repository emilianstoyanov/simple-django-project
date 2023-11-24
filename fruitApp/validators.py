from django.core.exceptions import ValidationError


def only_alphabet(value):
    if not all(i.isalpha() for i in value):
        raise ValidationError("Fruit name should contain only letters!")
