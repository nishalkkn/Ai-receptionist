from django.db import models
from doctor.models import Doctor
from patient.models import Patient

# Create your models here.


class Appointment(models.Model):
    appot_id = models.AutoField(primary_key=True)
    # doc_id = models.IntegerField()
    doc=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    # patient_id = models.IntegerField()
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'appointment'

