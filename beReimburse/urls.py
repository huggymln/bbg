from django.urls import path
from beReimburse import views

urlpatterns = [
    # Change status of reimburse
    path("reimburses/<str:reimburse_id>/accept", views.accept_reimburse, name="accept_reimburse"),
    path("reimburses/<str:reimburse_id>/reject", views.reject_reimburse, name="reject_reimburse"),
    path("reimburses/<str:reimburse_id>/on-progress", views.on_progress_reimburse, name="on_progress_reimburse"),

    # Etc
    path("", views.index, name="reimburse"),

]