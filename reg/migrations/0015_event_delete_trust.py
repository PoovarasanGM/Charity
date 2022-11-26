# Generated by Django 4.1.2 on 2022-11-07 04:32

from django.db import migrations, models
import reg.models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0014_trust'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('home', models.CharField(max_length=200, null=True)),
                ('event', models.CharField(max_length=200, null=True)),
                ('code', models.CharField(max_length=200, null=True, verbose_name=reg.models.code)),
            ],
        ),
        migrations.DeleteModel(
            name='Trust',
        ),
    ]
