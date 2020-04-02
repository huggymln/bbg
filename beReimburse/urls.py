from django.urls import path
from beReimburse import views

urlpatterns = [
    path("pisang/", views.index, name="reimburse"),
    path("reimburse/", views.index, name="reimburse"),

]