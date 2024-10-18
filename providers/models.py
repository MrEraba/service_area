from django.db import models

class LanguageChoices(models.TextChoices):
    ENGLISH = 'EN', 'English'
    SPANISH = 'SP', 'Spanish'


class CurrencyChoices(models.TextChoices):
    USD = 'USD', 'USD'
    EUR = 'EUR', 'EUR'


class Provider(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=12, default='')
    language = models.CharField(max_length=2, choices=LanguageChoices.choices, default=LanguageChoices.ENGLISH)
    currency = models.CharField(max_length=4, choices=CurrencyChoices.choices, default=CurrencyChoices.USD)