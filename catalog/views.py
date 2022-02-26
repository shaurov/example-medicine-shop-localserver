from django.shortcuts import render
from rest_framework import generics
from catalog.models import Medicine
from catalog.serializers import MedicineSerializer, MedicineSerializerFlattened


class Catalog(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializerFlattened


class MedicineList(generics.ListAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class MedicineDetail(generics.RetrieveAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

