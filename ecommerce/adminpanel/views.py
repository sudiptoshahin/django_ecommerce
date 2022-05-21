from django.shortcuts import render
from product.forms import ProductForm

# Create your views here.

def adminPanel(request):

    return render(request, 'adminpanel/index.html')


def addProduct(request):

    form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, 'adminpanel/add-product.html', context)