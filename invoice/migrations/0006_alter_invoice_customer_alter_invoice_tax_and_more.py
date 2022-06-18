# Generated by Django 4.0.5 on 2022-06-13 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0017_tax_alter_transfermoney_options_customer_and_more'),
        ('outcome_income', '0007_alter_incomes_customer_alter_outcomes_customer'),
        ('invoice', '0005_tax_customer_alter_invoice_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.customer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='tax',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.tax'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_customer', to='organization.customer'),
        ),
        migrations.AlterField(
            model_name='returnedproduct',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.customer'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Tax',
        ),
    ]
