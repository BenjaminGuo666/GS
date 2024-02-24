from django.urls import path
from .views import (
    ActivityListView,
    ActivityCreateView,
    ActivityUpdateView,
    ActivityDeleteView
)

urlpatterns = [
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activities/create/', ActivityCreateView.as_view(), name='activity_create'),
    path('activities/update/<int:pk>/', ActivityUpdateView.as_view(), name='activity_update'),
    path('activities/delete/<int:pk>/', ActivityDeleteView.as_view(), name='activity_delete'),
]
