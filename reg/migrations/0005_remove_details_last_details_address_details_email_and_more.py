# Generated by Django 4.1.2 on 2022-10-29 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_remove_details_food_details_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='last',
        ),
        migrations.AddField(
            model_name='details',
            name='address',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='events',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='mobile',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='pincode',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='price',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
