from django.urls import path

from operative.views import OperativesListView,OperativeCreateView

urlpatterns = [
    path('create-operative/', OperativeCreateView.as_view(), name='create_operative'),
    path('list-operatives/', OperativesListView.as_view(), name= 'list_operatives'),
]