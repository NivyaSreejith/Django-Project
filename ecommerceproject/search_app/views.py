from django.shortcuts import render
from shopapp.models import Product
from django.db.models import Q

def SearchResult(request):
    products = None
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'search.html', {'query': query, 'products': products})
