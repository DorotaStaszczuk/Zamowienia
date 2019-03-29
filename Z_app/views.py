from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from .models import Product, User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from .forms import MyUserCreationForm, LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MainSiteView(ListView):
    model = Product

    def get(self, request):
        product_list = Product.objects.all()
        paginator = Paginator(product_list, 5)

        page = request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        return render(request, 'main.html', {'products': products})

        # not working yet
        # def get_queryset(self):
        #     if request.method == 'GET':
        #         query = self.request.GET.get('q')
        #         if query:
        #             return Product.objects.filter(name__icontains=query)
        #         else:
        #             return Product.objects.all()


class ProductView(DetailView):
    model = Product


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'

    def get_success_url(self):
        return reverse('product', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(self.get_success_url())


class EditProductView(LoginRequiredMixin, UpdateView):
    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.user

    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('product', args=[self.object.pk])


class DeleteProductView(LoginRequiredMixin, DeleteView):
    def test_func(self):
        self.object = self.get_object()
        return self.request.user == self.object.user

    model = Product
    success_url = reverse_lazy("main")


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request=request, username=username, password=password)
            if user is None:
                form.add_error('login', 'Login lub hasło jest niepoprawne')
                return render(request, "login.html",
                              {'form': form})
            login(request, user)
            return redirect('main')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = MyUserCreationForm()
    return render(request, 'signup.html', {'form': form})


class UserView(LoginRequiredMixin, DetailView):
    model = User


class EditUserView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'email', 'profile_image')
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('user', args=[self.object.pk])


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("main")
