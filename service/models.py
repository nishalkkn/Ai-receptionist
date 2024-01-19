from django.db import models
from department.models import Department
# Create your models here.
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    # dept_id = models.IntegerField()
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'service'

