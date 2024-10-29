from django.urls import path
from .views import EquipmentListView,EquipmentDetailView,EquipmentCreateView,EquipmentUpdateView
from . import views

urlpatterns = [
    path('equiplist/', EquipmentListView.as_view(), name='equip_list'),
    path('<int:pk>/', EquipmentDetailView.as_view(), name='equip_detail'),
    path('new/', EquipmentCreateView.as_view(), name='equip_create'),
    path('<int:pk>/edit/', EquipmentUpdateView.as_view(), name='equip_edit'),
    path('query1/', views.query1, name='query1'),
    path('query2/', views.query2, name='query2'),
    path('queries/', views.QueryLinksView.as_view(), name='queries'),
]

