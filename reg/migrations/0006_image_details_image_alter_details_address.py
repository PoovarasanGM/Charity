# Generated by Django 4.1.2 on 2022-10-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0005_remove_details_last_details_address_details_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/%y')),
            ],
        ),
        migrations.AddField(
            model_name='details',
            name='image',
            field=models.ImageField(null=True, upload_to='images/%y'),
        ),
        migrations.AlterField(
            model_name='details',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
