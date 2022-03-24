from django.urls import path
from .views import PatientViews, PhysicianViews, UpcomingAppointmentsViews

urlpatterns = [
    path('patients/', PatientViews.as_view()),
    path('patients/<int:id>', PatientViews.as_view()),

    path('physicians/', PhysicianViews.as_view()),
    path('physicians/<int:id>', PhysicianViews.as_view()),

    path('appointments/', UpcomingAppointmentsViews.as_view()),
    path('appointments/<int:id>', UpcomingAppointmentsViews.as_view())


]