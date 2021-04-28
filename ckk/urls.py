from django.urls import path
from . import views

app_name = 'ckk'

urlpatterns = [
    path('', views.KKListView.as_view(), name='kk'),
]
