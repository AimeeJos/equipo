from django.urls import path, include
from assignment_2 import views

urlpatterns = [
    path("", views.ConsultationViews.as_view(), name="assign2"),
]
