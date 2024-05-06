# Generated by Django 4.2 on 2024-01-03 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0008_remove_zohomodules_reconciliation'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTermsUpdates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_action', models.IntegerField(default=0, null=True)),
                ('status', models.CharField(default='New', max_length=100, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('distributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.distributordetails')),
                ('payment_term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.paymentterms')),
            ],
        ),
    ]
