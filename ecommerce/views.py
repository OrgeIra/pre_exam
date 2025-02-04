from django.shortcuts import render

def product_list(request):
    return render(request, 'e-commerce\product\product-list.html')

def product_detail(request):
    return render(request, 'e-commerce\product\product-details.html')

def customers(request):
    return render(request, 'e-commerce\customers.html')

def custome_details(request):
    return render(request, 'e-commerce\customer-details.html')

