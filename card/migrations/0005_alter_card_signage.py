# Generated by Django 5.0.1 on 2024-01-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_alter_card_primary_contact_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='signage',
            field=models.FileField(upload_to='signage/'),
        ),
    ]