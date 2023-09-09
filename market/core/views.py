from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignUpForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile



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


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=pk)
        
        return render(request, 'core/profile.html', {'profile': profile})
    else:
        return redirect('home')
    
    
def update_profile(request):
	if request.user.is_authenticated:
		profile_user = Profile.objects.get(id=request.user.id)
		profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_user)
  
		if profile_form.is_valid():
			profile_form.save()

			return redirect('dashboard:index')
		return render(request, 'core/update_profile.html', {'profile_form': profile_form})
	else:
		return redirect('home')