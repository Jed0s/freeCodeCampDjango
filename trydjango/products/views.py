from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Product
#from .forms import ProductForm

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)

def product_detail_view(request, id):
    obj = Product.objects.get(id=id)
    context = {
        'object': obj,
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        obj.delete()
        return('../../')
    context = {
        'form': obj,
    }
    return render(request, 'products/product_delete.html', context)

'''
def render_initial_data(request):
    initial_data = {
        'title': "My awesome title"
    }
    obj = Product.objects.get(id=1)
    form = RawProductForm(request.POST or None, initial=initial_data, instance=obj) # ?
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

'''