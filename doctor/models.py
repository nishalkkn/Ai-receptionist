from django.db import models
from department.models import Department
# Create your models here.
from department.models import Department

class Doctor(models.Model):
    doct_id = models.AutoField(primary_key=True)
    doct_name = models.CharField(max_length=25)
    # dept_id = models.IntegerField()
    dept = models.ForeignKey(Department,on_delete=models.CASCADE)
    address = models.CharField(max_length=55)
    phone_no = models.CharField(max_length=10)
    email = models.CharField(max_length=55)
    experience = models.CharField(max_length=15)
    qualification = models.CharField(max_length=35)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'doctor'
