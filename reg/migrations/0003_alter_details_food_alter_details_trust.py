# Generated by Django 4.0.4 on 2022-10-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0002_details_date_of_birth_details_food_details_trust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='food',
            field=models.CharField(choices=[('Egg', 'Egg'), ('Food', 'Food'), ('BedSheets', 'BedSheets'), ('Stationary', 'Stationary'), ('Dress', 'Dress')], max_length=200),
        ),
        migrations.AlterField(
            model_name='details',
            name='trust',
            field=models.CharField(choices=[('MotherTeresa', 'MotherTeresa'), ('AnnaiTeresa', 'AnnaiTeresa'), ('BlindSchool', 'BlindSchool'), ('Henry', 'Henry'), ('DonBoscoAnbuIllam', 'DonBoscoAnbuIllam')], max_length=200),
        ),
    ]