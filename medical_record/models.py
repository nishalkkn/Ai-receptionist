from django.db import models
from doctor.models import Doctor
from appoinment.models import Appointment
from patient.models import Patient
# Create your models here.

class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    # doct_id = models.IntegerField()
    doct = models.ForeignKey(Doctor,models.CASCADE)
    # appo_id = models.IntegerField()
    appo = models.ForeignKey(Appointment,models.CASCADE)
    med_recd = models.CharField(max_length=450)

    class Meta:
        managed = False
        db_table = 'medical_record'

