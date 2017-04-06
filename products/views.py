# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm

from .models import Product

# Create your views here.

def hello_world(request):
	product = Product.objects.order_by('id')
	title = " Página de Inicio"
	template = loader.get_template('index.html')
	context = {
		'product':product,
		'title':title
	}
	return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = loader.get_template('product_detail.html')
    context = {
        'product': product
    }

    return HttpResponse(template.render(context, request))

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
