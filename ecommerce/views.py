from django.shortcuts import render, get_object_or_404
from ecommerce.models import Product

def product_list(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'e-commerce\product\product-list.html', context=context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk )
    context = {
        'product' : product
    }
    
    return render(request, 'e-commerce\product\product-details.html', context=context)

def customers(request):
    return render(request, 'e-commerce\customers.html')

def custome_details(request):
    return render(request, 'e-commerce\customer-details.html')

