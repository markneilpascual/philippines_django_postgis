from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from regions.models import Region


class RegionDetailView(DetailView):
    template_name = 'region-detail.html'
    model = Region


class RegionListView(ListView):
    model = Region
    template_name = 'region-search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        result = Region.objects.filter(Q(adm1alt1en=query))
        return result


class IndexView(TemplateView):
    template_name = 'region-search.html'
