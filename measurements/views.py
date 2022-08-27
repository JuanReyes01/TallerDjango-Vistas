from .logic import measurements_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurementss_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurements_dto = vl.get_measurements(id)
            measurements = serializers.serialize('json', [measurements_dto,])
            return HttpResponse(measurements, 'application/json')
        else:
            measurementss_dto = vl.get_measurementss()
            measurementss = serializers.serialize('json', measurementss_dto)
            return HttpResponse(measurementss, 'application/json')

    if request.method == 'POST':
        measurements_dto = vl.create_measurements(json.loads(request.body))
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

@csrf_exempt
def measurements_view(request, pk):
    if request.method == 'GET':
        measurements_dto = vl.get_measurements(pk)
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')

    if request.method == 'PUT':
        measurements_dto = vl.update_measurements(pk, json.loads(request.body))
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')
    
    if request.method == 'DELETE':
        measurements_dto = vl.delete_measurements(pk)
        measurements = serializers.serialize('json', [measurements_dto,])
        return HttpResponse(measurements, 'application/json')
        