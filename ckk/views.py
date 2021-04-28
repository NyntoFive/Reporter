from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CKKItem, CKKImage

class KKListView(ListView):
    template_name = "ckk/item_list.html"
    model = CKKItem

    

