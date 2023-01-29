from django.urls import path

from logistics.views import logistic_update,LogisticsListView,LogisticsCreateView

urlpatterns = [
    path('create-logistic/',LogisticsCreateView.as_view(), name='create_logistic'),
    path('list-logistics/',LogisticsListView.as_view(), name='list_logistics'),
    path('update-logistic/<int:pk>/', logistic_update, name ='update_logistic'),
]