from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializer import TextSerializer, ColorSerializer
from rest_framework.parsers import JSONParser
from .models import Text, Color
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@csrf_exempt
def color_update(request):
    obj = Color.objects.get(pk=1)
    data = JSONParser().parse(request)
    serializer = ColorSerializer(obj, data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def color_output(request):
    obj = Color.objects.get(pk=1)
    serializer = ColorSerializer(obj)
    return JsonResponse(serializer.data, status=201)

@csrf_exempt
def text_insert(request):
    data = JSONParser().parse(request)
    serializer = TextSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    if Text.objects.filter(pk=data["pid"]).count() > 0:
        s = "There already exists " + str(data["pid"]) + "instance"
        return JsonResponse({"error": s}, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def text_update(request):
    data = JSONParser().parse(request)
    try:
        obj = Text.objects.get(pk=data["pid"])
    except Text.DoesNotExist:
        serializer = TextSerializer(data=data)
        if serializer.is_valid():
            s = "There is no " + str(data["pid"]) + "instance"
            return JsonResponse({"error": s}, status=201)
        return JsonResponse({}, status=400)

    if obj.ptext == data["ptext"]:
        s = "There already saves " + data["ptext"] + " instance"
        return JsonResponse({"error": s}, status=201)
    serializer = TextSerializer(obj, data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def text_delete(request):
    data = JSONParser().parse(request)
    try:
        obj = Text.objects.get(pk=data["pid"])
    except Text.DoesNotExist:
        serializer = TextSerializer(data=data)
        if serializer.is_valid():
            s = "There is no " + str(data["pid"]) + "instance"
            return JsonResponse({"error": s}, status=201)
        return JsonResponse(serializer.errors, status=400)

    serializer = TextSerializer(obj, data=data)

    if serializer.is_valid():
        obj.delete()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)