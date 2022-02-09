from django.urls import path
from regions.views import RegionDetailView, RegionListView, IndexView

urlpatterns = [
    path('RegionDetailView/<int:pk>', RegionDetailView.as_view(), name='region-detail-view'),
    path('RegionListView/', RegionListView.as_view(), name='region-list'),
    path('', IndexView.as_view(), name='index'),
]