# Generated by Django 3.1.1 on 2020-09-12 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_company_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reports.company'),
        ),
    ]
