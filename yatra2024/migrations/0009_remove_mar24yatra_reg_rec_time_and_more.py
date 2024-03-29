# Generated by Django 4.2.6 on 2024-01-22 12:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yatra2024', '0008_remove_mar24yatra_reg_confirm_time'),
    ]

    operations = [

        migrations.AlterField(
            model_name='mar24yatra_reg',
            name='fR_Mob',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(limit_value=10, message='Mobile number must be 10 digits.'), django.core.validators.MaxLengthValidator(limit_value=10, message='Mobile number must be 10 digits.')]),
        ),
    ]
