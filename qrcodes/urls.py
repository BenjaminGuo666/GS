from django.urls import path
from .views import ActivityListView, ActivityDetailView, ActivityCreateView, ActivityUpdateView, ActivityDeleteView

urlpatterns = [
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activities/<int:pk>/', ActivityDetailView.as_view(), name='activity_detail'),
    path('activities/new/', ActivityCreateView.as_view(), name='activity_new'),
    path('activities/<int:pk>/edit/', ActivityUpdateView.as_view(), name='activity_edit'),
    path('activities/<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity_delete'),
]
