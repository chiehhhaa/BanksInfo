from django.urls import path
from . import views
from django.urls import path, re_path
from django.views.generic import TemplateView

app_name = "banks"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/banks/", views.bank_list, name="list"),
    path("api/banks/<int:bank_id>/branches/", views.bank_branches, name="branches"),
    path("api/branches/<int:branch_id>/", views.branch_detail, name="branch_detail"),
]

