from django import forms
from assignment_2.models import Consultation


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = [
            "ip",
            "clinic_name",
            "logo",
            "physician_name",
            "physician_contact",
            "patient_first",
            "patient_last",
            "patient_dob",
            "patient_contact",
            "chief_complaint",
            "consultation_note",
        ]
        widgets = {
            "ip": forms.TextInput(attrs={"class": "form-control", "placeholder": "IP"}),
            "clinic_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Clinic Name"}
            ),
            "physician_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Physician Name"}
            ),
            "physician_contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Physician Contact"}
            ),
            "patient_first": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Patient First Name"}
            ),
            "patient_last": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Patient Last Name"}
            ),
            "patient_dob": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "patient_contact": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Patient Contact"}
            ),
            "chief_complaint": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Chief Complaint",
                }
            ),
            "consultation_note": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Consultation Note",
                }
            ),
        }
        labels = {
            "ip": "IP",
            "clinic_name": "Clinic Name",
            "logo": "Clinic Logo",
            "physician_name": "Physician Name",
            "physician_contact": "Physician Contact",
            "patient_first": "Patient First Name",
            "patient_last": "Patient Last Name",
            "patient_dob": "Patient DOB",
            "patient_contact": "Patient Contact",
            "chief_complaint": "Chief Complaint",
            "consultation_note": "Consultation Note",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        exclude_required = ["chief_complaint", "consultation_note"]
        for field_name, field in self.fields.items():
            if field_name not in exclude_required:
                field.required = True
