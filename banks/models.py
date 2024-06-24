from django.db import models


class Bank(models.Model):
    bank_code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bank_code} - {self.name}"


class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name="branches", on_delete=models.CASCADE)
    branch_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.bank.bank_code} - {self.branch_code} - {self.name}"
