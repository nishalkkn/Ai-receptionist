# Generated by Django 3.2.20 on 2024-01-06 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=29)),
                ('password', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=49)),
                ('uid', models.IntegerField()),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]