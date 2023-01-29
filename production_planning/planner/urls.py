from django.urls import path

from planner.views import  planner_update ,PlannerDeletView,PlannersListView,PlannerCreateView

urlpatterns = [
    path('create-planner/',PlannerCreateView.as_view(), name='create_planner'),
    path('list-planners/',PlannersListView.as_view(), name= 'list_planners'),
    path('update-planner/<int:pk>/', planner_update, name = 'update_planner'),
    path('delete-planner/<int:pk>/', PlannerDeletView.as_view(), name= 'delete_planner'),
]