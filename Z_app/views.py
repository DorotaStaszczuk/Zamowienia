from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

class MainSiteView(ListView):
    model = Product
    paginate_by = 50

    def get(self, request):
        ctx = {'products': Product.objects.all()}
        return render(request, 'main.html', ctx)

class ProductView(DetailView):
    model = Product

class AddProductView(CreateView):
    model = Product
    fields = '__all__'

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())
