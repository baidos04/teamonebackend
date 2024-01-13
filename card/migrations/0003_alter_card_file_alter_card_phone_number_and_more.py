# Generated by Django 5.0.1 on 2024-01-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_card_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='card',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='card',
            name='primary_contact_info',
            field=models.IntegerField(max_length=100),
        ),
    ]