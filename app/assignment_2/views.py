from django.shortcuts import render, redirect
from assignment_2.forms import ConsultationForm
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from assignment_2.generate_pdf import generate_pdf
from common.helpers import download_file
from django.conf import settings

from django.views.generic import View
from assignment_2.models import Consultation
import os

# labels = {
#     "ip": "IP ADDRESS",
#     "clinic_name": "CLINIC NAME",
#     "logo": "LOGO",
#     "physician_name": "PHYSICIAN NAME",
#     "physician_contact": "PHYSICIAN CONTACT",
#     "patient_first": "PATIENT FIRST",
#     "patient_last": "PATIENT LAST",
#     "patient_dob": "PATIENT DOB",
#     "patient_contact": "PATIENT CONTACT",
#     "chief_complaint": "CHIEF COMPLAINT",
#     "consultation_note": "CONSULTAION NOTE",
# }


class ConsultationViews(View):

    def get(self, request):
        form = ConsultationForm()
        context = {"form": form}
        return render(request, "assign2.html", context)

    @csrf_exempt
    def post(self, request):
        form = ConsultationForm(request.POST, request.FILES)
        errors = []

        physician_contact = request.POST.get("physician_contact")
        patient_contact = request.POST.get("patient_contact")
        
        if len(physician_contact) != 10:
            errors.append(
                {
                    "label": "Physician contact ",
                    "help_text": "Physician contact should have 10 digits",
                }
            )
        if len(patient_contact) != 10:
            errors.append(
                {
                    "label": "Patient contact",
                    "help_text": "Patient contact should have 10 digits",
                }
            )
        else:
            if form.is_valid():
                print("valid form")
                form_data = form.cleaned_data

                consultation = form.save()
                consultation.logo = request.FILES.get("logo")
                consultation.save()

                data = {
                    "IP ADDRESS": consultation.ip,
                    "CLINIC NAME": consultation.clinic_name,
                    "LOGO": str(consultation.logo.url).split("/")[-1],
                    "PHYSICIAN NAME": consultation.physician_name,
                    "PHYSICIAN CONTACT": consultation.physician_contact,
                    "PATIENT FIRST": consultation.patient_first,
                    "PATIENT LAST": consultation.patient_last,
                    "PATIENT DOB": str(consultation.patient_dob),
                    "PATIENT CONTACT": consultation.patient_contact,
                    "CHIEF COMPLAINT": consultation.chief_complaint,
                    "CONSULTAION NOTE": consultation.consultation_note,
                }
                filename = generate_pdf(data)
                print("FILE: ", filename)
                response = download_file("REPORTS", filename)
                return response

        context = {"form": form, "errors": errors}
        return render(request, "assign2.html", context)
