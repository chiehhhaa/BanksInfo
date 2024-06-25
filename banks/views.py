from django.shortcuts import render
from .models import Bank, Branch
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def index(request):
    banks = Bank.objects.filter()
    return render(request, "banks/index.html", {"banks": banks})


def bank_list(request):
    banks = Bank.objects.all()
    data = [
        {"id": bank.id, "bank_code": bank.bank_code, "name": bank.name}
        for bank in banks
    ]
    return JsonResponse(data, safe=False)


def bank_branches(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    branches = bank.branches.all()
    data = [{"id": branch.id, "name": branch.name, "branch_code": branch.branch_code} for branch in branches]
    return JsonResponse(data, safe=False)


def branch_detail(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    data = {
        "branch_code": branch.branch_code,
        "address": branch.address,
        "phone": branch.phone,
    }
    return JsonResponse(data)
