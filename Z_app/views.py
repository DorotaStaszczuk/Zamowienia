from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from django.views.generic.list import ListView


class MainSiteView(ListView):
    model = Product
    paginate_by = 50

    def get(self, request):
        ctx = {'products': Product.objects.all()}
        return render(request, 'main.html', ctx)
