# Generated by Django 4.2 on 2024-01-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0012_paymenttermsupdates_interested_to_continue'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
