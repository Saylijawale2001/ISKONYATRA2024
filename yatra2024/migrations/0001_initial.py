# Generated by Django 4.2.6 on 2024-01-21 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mar24YatraReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fR_Name', models.CharField(max_length=255)),
                ('fR_age', models.CharField(max_length=255)),
                ('fR_gender', models.CharField(max_length=255)),
                ('fR_Mob', models.CharField(max_length=255)),
                ('fR_chant', models.CharField(max_length=255)),
                ('consellor_Name', models.CharField(max_length=255)),
                ('no_of_Rooms', models.CharField(max_length=255)),
                ('room_cost', models.CharField(max_length=255)),
                ('yatra_type', models.CharField(max_length=255)),
                ('travelling_From', models.CharField(max_length=255)),
                ('transport_Mode', models.CharField(max_length=255)),
                ('coach_number', models.CharField(max_length=255)),
                ('return_Transport_Mode', models.CharField(max_length=255)),
                ('return_coach_number', models.CharField(max_length=255)),
                ('any_Comments', models.CharField(max_length=255)),
                ('m1_name', models.CharField(max_length=255)),
                ('m1_age', models.CharField(max_length=255)),
                ('m1_gender', models.CharField(max_length=255)),
                ('m2_name', models.CharField(max_length=255)),
                ('m2_age', models.CharField(max_length=255)),
                ('m2_gender', models.CharField(max_length=255)),
                ('m3_name', models.CharField(max_length=255)),
                ('m3_age', models.CharField(max_length=255)),
                ('m3_gender', models.CharField(max_length=255)),
                ('m4_name', models.CharField(max_length=255)),
                ('m4_age', models.CharField(max_length=255)),
                ('m4_gender', models.CharField(max_length=255)),
                ('m5_name', models.CharField(max_length=255)),
                ('m5_age', models.CharField(max_length=255)),
                ('m5_gender', models.CharField(max_length=255)),
                ('m6_name', models.CharField(max_length=255)),
                ('m6_age', models.CharField(max_length=255)),
                ('m6_gender', models.CharField(max_length=255)),
                ('m7_name', models.CharField(max_length=255)),
                ('m7_age', models.CharField(max_length=255)),
                ('m7_gender', models.CharField(max_length=255)),
            ],
        ),
    ]
