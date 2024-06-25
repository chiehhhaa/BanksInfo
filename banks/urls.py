from django.urls import path
from . import views

app_name = "banks"

urlpatterns = [
    path("", views.index, name="index"),
    path("api/banks/", views.bank_list, name="list"),
    path("api/banks/<int:bank_id>/branches/", views.bank_branches, name="branches"),
    path("api/branches/<int:branch_id>/", views.branch_detail, name="branch_detail"),
    path(
        '<str:bank_code>/<str:branch_code>/<str:bank_name>-<str:branch_name>.html',
        views.bank_branch_detail,
        name='bank_branch_detail'
    ),
]

