# Generated by Django 3.1.1 on 2020-09-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20200913_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='company_types',
            field=models.CharField(choices=[('ГО', 'ГО'), ('ФЛ', 'ФЛ')], default='ГО', max_length=3),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='inn',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='kpp',
            field=models.IntegerField(null=True),
        ),
    ]
