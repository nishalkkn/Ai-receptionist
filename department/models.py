from django.db import models

# Create your models here.

class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=49)

    class Meta:
        managed = False
        db_table = 'department'

