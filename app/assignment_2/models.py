from django.db import models
from django.core.validators import RegexValidator


class Consultation(models.Model):
    ip = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[RegexValidator(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")],
        help_text="Enter a valid IP address.",
    )
    clinic_name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.ImageField(
        upload_to="logos/", null=True, blank=True
    )  # Assuming you want to store logos as image files
    physician_name = models.CharField(max_length=255, null=True, blank=True)
    physician_contact = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[RegexValidator(r"^\d{1,10}$")],
        help_text="Enter a valid 10-digit phone number.",
    )
    patient_first = models.CharField(max_length=255, null=True, blank=True)
    patient_last = models.CharField(max_length=255, null=True, blank=True)
    patient_dob = models.DateField(null=True, blank=True)
    patient_contact = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        validators=[RegexValidator(r"^\d{1,10}$")],
        help_text="Enter a valid 10-digit phone number.",
    )
    chief_complaint = models.TextField(null=True, blank=True)
    consultation_note = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
