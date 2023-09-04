from django.shortcuts import render
from item.models import Category, Item



# Create your views here.
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    
    context = {'items': items, 'categories': categories}
    return render(request, 'core/index.html', context)


def contact(request):
    return render(request, 'core/contact.html')