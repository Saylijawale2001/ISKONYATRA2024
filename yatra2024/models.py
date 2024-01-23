# models.py
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class mar24yatra_reg(models.Model):
    fR_Name = models.CharField(max_length=255)
    fR_age = models.CharField(max_length=255)
    fR_gender = models.CharField(max_length=255)
    fR_Mob = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(limit_value=10, message="Mobile number must be 10 digits."),
            MaxLengthValidator(limit_value=10, message="Mobile number must be 10 digits."),
        ],
        unique=True)
    fR_chant = models.CharField(max_length=255)
    consellor_Name = models.CharField(max_length=255)
    no_of_Rooms = models.CharField(max_length=255)
    room_cost = models.CharField(max_length=255)
    yatra_type = models.CharField(max_length=255)
    travelling_From = models.CharField(max_length=255)
    transport_Mode = models.CharField(max_length=255)
    coach_number = models.CharField(max_length=255)
    return_Transport_Mode = models.CharField(max_length=255)
    return_coach_number = models.CharField(max_length=255)
    any_Comments = models.CharField(max_length=255)
    m1_name = models.CharField(max_length=255)
    m1_age = models.CharField(max_length=255)
    m1_gender = models.CharField(max_length=255)
    m2_name = models.CharField(max_length=255)
    m2_age = models.CharField(max_length=255)
    m2_gender = models.CharField(max_length=255)
    m3_name = models.CharField(max_length=255)
    m3_age = models.CharField(max_length=255)
    m3_gender = models.CharField(max_length=255)
    m4_name = models.CharField(max_length=255)
    m4_age = models.CharField(max_length=255)
    m4_gender = models.CharField(max_length=255)
    m5_name = models.CharField(max_length=255)
    m5_age = models.CharField(max_length=255)
    m5_gender = models.CharField(max_length=255)
    m6_name = models.CharField(max_length=255)
    m6_age = models.CharField(max_length=255)
    m6_gender = models.CharField(max_length=255)
    m7_name = models.CharField(max_length=255)
    m7_age = models.CharField(max_length=255)
    m7_gender = models.CharField(max_length=255)

    class Meta:
        db_table = 'mar24yatra_reg'


class yatrauser(models.Model):
    name = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    client_id =models.CharField(max_length=45)
    role = models.CharField(max_length=45)
    password = models.CharField(max_length=45)  # Assuming password is not nullable
    SrNo = models.AutoField(primary_key=True)  # Assuming SrNo is auto-incremented and a primary key

    class Meta:
        db_table = 'YatraUser'