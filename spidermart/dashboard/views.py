
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Item, Category

@login_required
def index(request):
    user = request.user
    items = Item.objects.filter(created_by=request.user)
    categories = Category.objects.all()

    # Get the count of items in each category for the current user
    # category_counts = {
    #     category.id: Item.objects.filter(category=category, created_by=user).count()
    #     for category in categories
    # }
    # Calculate the count of items in each category for the current user
    category_counts = {
        category.id: items.filter(category=category).count() for category in categories
    }



    return render(request, 'dashboard/index.html', {
        'items': items,
        'categories': categories,
        'category_counts': category_counts,


    })

     

    

   

