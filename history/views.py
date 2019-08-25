from django.http import JsonResponse
import json
import objectpath
from django.shortcuts import get_object_or_404, render
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

# Create your views here.

from .models import Materials, ThrownTrash
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




class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, material_id=1, format=None):
        material = ThrownTrash.objects.all()
        material = serializers.serialize('json',material)

        return HttpResponse(material, content_type="application/json")
        #return Response(data)












    