import csv
import re
from django.core.management.base import BaseCommand
from banks.models import Bank, Branch


class Command(BaseCommand):
    help = "Import bank and branch data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def get_head(self, institution):
        match institution:
            case _ if "代表人辦事處" in institution:
                return f'{institution.split("代表人辦事處")[0]}代表人辦事處'
            case _ if "銀行" in institution:
                return f'{institution.split("銀行")[0]}銀行'
            case _ if "信用合作社" in institution:
                return f'{institution.split("信用合作社")[0]}信用合作社'

    def extract_bank_and_branch(self, bank_branch_name):
        bank_keywords = ["銀行", "合作社"]
        pattern = rf"^(.+?)({'|'.join(bank_keywords)})(.+?(分行|支行|部|處|分社)?)?$"
        match = re.match(pattern, bank_branch_name)

        if match:
            bank_name = match.group(1).strip() + match.group(2).strip()
            branch_name = match.group(3).strip() if match.group(3) else ""
        else:
            bank_name = bank_branch_name.strip()
            branch_name = ""

        return bank_name, branch_name

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]

        with open(file_path, encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                head_code = row.get("\ufeff總機構代號", "")
                if len(head_code) < 3:
                    head_code = head_code.zfill(3)

                institution = row.get("機構名稱", "")
                head = self.get_head(institution)
                self.stdout.write(f"Institution: {institution}, Head: {head}")

                if head is None:
                    continue

                branch_code = row.get("機構代號", "")
                if not branch_code:
                    continue

                bank_name, branch_name = self.extract_bank_and_branch(institution)

                bank, created = Bank.objects.get_or_create(
                    bank_code=head_code, defaults={"name": head}
                )

                branch = Branch.objects.create(
                    bank=bank,
                    branch_code=branch_code,
                    name=branch_name,
                    address=row.get("地址", ""),
                    phone=row.get("電話", ""),
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        'Successfully imported data from "%s"' % file_path
                    )
                )
