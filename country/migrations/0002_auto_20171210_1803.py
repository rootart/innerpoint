# Generated by Django 2.0 on 2017-12-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='iso_2_digit',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='iso_3_digit',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]