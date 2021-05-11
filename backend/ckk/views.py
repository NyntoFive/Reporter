from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CKKItem, CKKImage

class KKListView(ListView):
    template_name = "ckk/item_list.html"
    model = CKKItem

    

def kk_list(request):
    products = CKKItem.objects.all()
    images=[]
    for i, d in enumerate(products):
        item = {products[i].sku: [img for img in products[i].all_images]}
        images.append(item)

    return render(request, 'ckk/detail.html', {"images": images})
