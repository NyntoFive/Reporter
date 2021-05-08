from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CKKItem, CKKImage

class KKListView(ListView):
    template_name = "ckk/item_list.html"
    model = CKKItem

    

def kk_list(request):
    products = CKKItem.objects.all()
    product_list = []

    for product in products:
        images = product.image_set.all()

        if images:
            product_
