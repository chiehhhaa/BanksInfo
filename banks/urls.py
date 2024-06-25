from django.urls import path
from . import views

app_name = "banks"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/banks/", views.bank_list, name="bank_list"),
    path(
        "api/banks/<int:bank_id>/branches/", views.bank_branches, name="bank_branches"
    ),
    path("api/branches/<int:branch_id>/", views.branch_detail, name="branch_detail"),
]
