"""Zamowienia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Z_app.views import MainSiteView, ProductView, AddProductView, EditProductView, \
DeleteProductView, LoginView, LogoutView, signup, UserView, EditUserView, DeleteUserView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/', MainSiteView.as_view(), name='main'),
    url(r'^product/(?P<pk>(\d)+)/$', ProductView.as_view(), name="product"),
    url(r'^add_product$', AddProductView.as_view(), name="add-product"),
    url(r'^edit_product/(?P<pk>\d+)/$', EditProductView.as_view(), name="edit-product"),
    url(r'^delete_product/(?P<pk>(\d)+)/$', DeleteProductView.as_view(), name="delete-product"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', LogoutView.as_view(), name="logout"),
    url(r'^signup$', signup, name="signup"),
    url(r'^user/(?P<pk>\d+)/$', UserView.as_view(), name="user"),
    url(r'^edit_user/(?P<pk>\d+)/$', EditUserView.as_view(), name="edit-user"),
    url(r'^delete_user/(?P<pk>(\d)+)/$', DeleteUserView.as_view(), name="delete-user"),

]
