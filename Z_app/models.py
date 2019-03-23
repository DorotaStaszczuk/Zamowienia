from django.db import models
from django.contrib.auth.models import User


USER_TYPE_CHOICES = (
    (0, 'Sprzedawca'),
    (1, 'Klient'),
    )

class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa")
    manufacturer = models.CharField(max_length=64, verbose_name="Producent")
    description = models.TextField(verbose_name="Opis")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Cena")
    image = models.ImageField(null=True, blank=True, verbose_name="Zdjęcie")

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Klient")
    product_list = models.TextField(verbose_name="Lista produktów")
    date_added = models.DateTimeField(auto_now_add=True, verbose_name="Data wprowadzenia")
    payment_deadline = models.DateTimeField(verbose_name="Termin_platnosci")
    total_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Sumaryczna cena")
    products = models.ManyToManyField(Product)

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, choices=USER_TYPE_CHOICES, verbose_name="Użytkownik")
    company_name = models.CharField(max_length=90, blank=True, verbose_name="Nazwa firmy")
    name = models.CharField(max_length=64, verbose_name="Imię")
    surname= models.CharField(max_length=64, verbose_name="Nazwisko")
    street = models.CharField(max_length=350, verbose_name="Ulica")
    house_number = models.IntegerField(verbose_name="Numer domu")
    apartment_number = models.PositiveSmallIntegerField(verbose_name="Numer lokalu")
    zip_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=350, verbose_name="Miejscowość")
