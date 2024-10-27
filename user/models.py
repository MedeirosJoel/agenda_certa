from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Numeros de telefone devem ser no formato: '+999999999'. Até 15 digitos são permitidos.")

cep_regex = RegexValidator(
    regex=r'/^d{5}(-d{3})?$/',
    message='CEPs devem ser no formato: 999999-999.')


class ServedCities(models.TextChoices):
    FLORIANOPOLIS = 'FL', 'Florianópolis'
    SAO_JOSE = 'SJ', 'São José'
    PALHOCA = 'PA', 'Palhoça'


class Client(models.base):
    id = models.Index()
    public_id = models.UUIDField()
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone_number = models.CharField(validators=phone_regex)

    address = models.CharField(max_length=512)
    cep = models.CharField(validators=cep_regex)
    city = models.TextChoices(ServedCities)

    salty