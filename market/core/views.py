from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm
from django.contrib.auth import authenticate, login



# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    
    context = {'items': items, 'categories': categories}
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})