from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    address = models.CharField(max_length=55)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=15)
    user_id = models.IntegerField()
    phone_no = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'patient'

