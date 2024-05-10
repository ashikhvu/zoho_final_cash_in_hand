# Generated by Django 3.2.23 on 2024-05-10 06:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0017_alter_trialperiod_interested_in_buying'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company_Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashInHandHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=50)),
                ('cih', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.cashinhand')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
