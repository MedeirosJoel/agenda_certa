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


class Client(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    public_id = models.UUIDField(auto_created=True)
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    phone_number = models.CharField(validators=[phone_regex], max_length=15)

    address = models.CharField(max_length=512)
    cep = models.CharField(validators=[cep_regex],  max_length=16)
    city = models.CharField(max_length=2, choices=ServedCities.choices, default=ServedCities.FLORIANOPOLIS)
