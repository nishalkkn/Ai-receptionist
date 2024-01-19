from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=25)
    address = models.CharField(max_length=55)
    e_mail = models.CharField(db_column='e-mail', max_length=30)  # Field renamed to remove unsuitable characters.
    phone_no = models.CharField(db_column='phone no', max_length=10)  # Field renamed to remove unsuitable characters.
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'

