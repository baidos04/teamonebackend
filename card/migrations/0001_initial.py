# Generated by Django 5.0.1 on 2024-01-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=155)),
                ('contact_number', models.CharField(max_length=100)),
                ('mc_dot_number', models.CharField(max_length=155)),
                ('number_or_trucks', models.CharField(max_length=100)),
                ('fuel_cards_register', models.CharField(max_length=100)),
                ('mailing_address', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('primary_contact_info', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=170)),
                ('file', models.FileField(upload_to='files/')),
                ('signature', models.ImageField(upload_to='signature/')),
            ],
        ),
    ]
