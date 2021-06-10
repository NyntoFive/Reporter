from .views import ImageViewSet
from rest_framework import routers
from django.urls import path, include
from . import views

app_name = 'ckk'
router = routers.DefaultRouter()
router.register(r'images', ImageViewSet)
urlpatterns = [
    path('api', include(router.urls)),
    path('kk', views.KKListView.as_view(), name='kk'),
    
    path(
        'new_item',
        views.CKKItemFormView.as_view(),
        name='new_item_form'
    ),
    path(
        'entry_success',
        views.CKKFormSuccessView.as_view(),
        name='form_success'
    )
]
