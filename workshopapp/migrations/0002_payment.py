# Generated by Django 4.0.6 on 2022-10-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Card_number', models.CharField(max_length=12)),
                ('Expiry_Date', models.CharField(max_length=4)),
                ('Cvv', models.CharField(max_length=3)),
            ],
        ),
    ]