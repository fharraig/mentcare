from django.urls import path
from .views import PatientViews

urlpatterns = [
    path('patients/', PatientViews.as_view()),
    path('patients/<int:id>', PatientViews.as_view())
]