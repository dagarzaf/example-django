# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import (
	render,
	get_object_or_404,
	redirect)
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import ProductForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from.mixins import LoginRequiredMixin

from .models import Product

# Create your views here.

class ProductList(ListView):
	model = Product

class ProductDetail(LoginRequiredMixin, DetailView):
	model = Product

#def product_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
#    template = loader.get_template('product_detail.html')
#    context = {
#        'product': product
#    }

#    return HttpResponse(template.render(context, request))


@login_required()
def new_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save(commit=False)
			product.save()
			return HttpResponseRedirect('/')
	else:
		form = ProductForm()

	template = loader.get_template('new_product.html')
	title = "New Product"
	context = {
		'form':form,
		'title':title
	}

	return HttpResponse(template.render(context, request))

def auth_login(request):
	if request.method == 'POST':
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		if action == 'signup':
			user = User.objects.create_user(username=username, password=password)
			user.save()
		elif  action == 'login':
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/')
	context = {}
	return render(request, 'login/login.html', context)
