from django.urls import path
from catalog.views import Catalog, MedicineList, MedicineDetail


urlpatterns = [
    path('', Catalog.as_view()),
    path('medicines/', MedicineList.as_view()),
    path('medicines/<int:pk>/', MedicineDetail.as_view()),
]

