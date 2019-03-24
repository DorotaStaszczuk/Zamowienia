from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class MainSiteView(ListView):
    model = Product
    paginate_by = 50

    def get(self, request):
        ctx = {'products': Product.objects.all()}
        return render(request, 'main.html', ctx)

class ProductView(DetailView):
    model = Product
