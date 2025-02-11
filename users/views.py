from django.shortcuts import render, get_object_or_404, redirect
from users.models import UserProfile
from users.forms import UserProfileForm
from django.http import HttpResponseNotFound


# Create your views here. 

def customer_list(request):
    users = UserProfile.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'users/customer_list.html', context)

def customer_detail(request, pk):
    user = get_object_or_404(UserProfile, id=pk)
    context = {
        'user': user,
    }
    return render(request, 'users/customer_details.html', context)

def add_customer(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = UserProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'users/add_customer.html', context)

def update_customer(request, pk ):
    user = get_object_or_404(UserProfile, id=pk)
    form = UserProfileForm(instance=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES,instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            return redirect('customer_detail', pk=pk)
    else:
        form = UserProfileForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'users/edit_customer.html', context)


def delete_customer(request, pk):
    try:
        user = UserProfile.objects.get(id=pk)
        print(f"User found: {user}")
    except UserProfile.DoesNotExist:
        print(f"User with ID {pk} does not exist")
        return HttpResponseNotFound(f"User with ID {pk} does not exist")

    if request.method == 'POST':
        user.delete()
        return redirect('customer-list')

    context = {'user': user}
    return render(request, 'users/delete_customer.html', context)
