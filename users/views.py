from django.shortcuts import render
from users.models import UserProfile

# Create your views here.
def customers(request):
    users = UserProfile.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'users\customers.html', context=context)  

def custome_details(request):
    return render(request, 'users\customer-details.html') 
