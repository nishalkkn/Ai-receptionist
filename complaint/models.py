from django.db import models
from user.models import User

# Create your models here.
class Complaint(models.Model):
    comp_id = models.AutoField(primary_key=True)
    # user_id = models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    complaint = models.CharField(max_length=105)
    replay = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'complaint'

