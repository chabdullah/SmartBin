from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .models import Materials
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'history/index.html'
    context_object_name = 'material_list'

    def get_queryset(self):
        """
        Return the different kind of bins
        """
        return Materials.objects.all()
    
def detail(request, material_id):
    material = get_object_or_404(Materials, pk=material_id) # sono parametri del modello

    return render(request, 'history/detail.html', {'material': material})
    
    
def update(request, material_id, mesured_weight):
    material = get_object_or_404(Materials, pk=material_id)
    
    new_trash = material.throwntrash_set.create(weight=mesured_weight, thrown_date=timezone.now())
    
    return HttpResponse("Database updated")
    