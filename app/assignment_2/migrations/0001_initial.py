# Generated by Django 3.2.25 on 2024-03-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=100, null=True)),
                ('clinic_name', models.CharField(blank=True, max_length=255, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('physician_name', models.CharField(blank=True, max_length=255, null=True)),
                ('physician_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('patient_first', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_last', models.CharField(blank=True, max_length=255, null=True)),
                ('patient_dob', models.DateField(blank=True, null=True)),
                ('patient_contact', models.CharField(blank=True, max_length=100, null=True)),
                ('chief_complaint', models.TextField(blank=True, null=True)),
                ('consultation_note', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
