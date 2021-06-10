from rest_framework import viewsets
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views import View
from .forms import CKKForm
from . import serializers

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CKKItem, CKKImage

class KKListView(ListView):
    template_name = "ckk/item_list.html"
    model = CKKItem

class CKKItemFormView(FormView):
    template_name = "ckk/ckkitem_form.html"
    form_class = CKKForm

    success_url = '/entry_success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CKKFormSuccessView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Item record saved successfully")

#############################################################################
# DRF / API
class ApiImageList(ListCreateAPIView):
    queryset = CKKImage.objects.all()
    serializer_class = serializers.ImageSerializer

class ApiImageDetail(RetrieveUpdateDestroyAPIView):
    queryset = CKKImage.objects.all()
    serializer_class = serializers.ImageSerializer

class ApiImageViewSet(viewsets.ModelViewSet):
    queryset = CKKImage.objects.all()
    serializer_class = serializers.ImageSerializer