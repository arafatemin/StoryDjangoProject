# Generated by Django 4.0.5 on 2022-06-13 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0022_productcategory_slug_and_more'),
        ('organization', '0014_seller_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('inv_no', models.CharField(blank=True, max_length=128, null=True)),
                ('datetime', models.DateTimeField()),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_customer', to='organization.customer')),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.tax')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice_user', to='organization.seller')),
            ],
        ),
        migrations.CreateModel(
            name='SoldProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.IntegerField()),
                ('price', models.IntegerField()),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.seller')),
            ],
            options={
                'verbose_name': 'Products In Invoice',
            },
        ),
        migrations.CreateModel(
            name='ReturnedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('sold_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.soldproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('amount', models.FloatField()),
                ('note', models.TextField(blank=True, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice_payment_bank', to='organization.bank')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_INVOICE_user', to='organization.seller')),
            ],
            options={
                'verbose_name': 'Payments For Invoice',
            },
        ),
    ]
