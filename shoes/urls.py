from django.urls import path
from .views import ShoesList, ShoesDetail

urlpatterns = [
    path('', ShoesList.as_view(), name='shoes_list'),
    path('<int:pk>/', ShoesDetail.as_view(), name='shoes_detail'),
]