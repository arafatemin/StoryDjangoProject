# Generated by Django 4.0.5 on 2022-06-13 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0016_alter_transfermoney_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='transfermoney',
            options={'verbose_name': 'Take Money'},
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='customer_images/')),
                ('phone_number', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('belongs_to_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='belongs_to_seller', to='organization.seller')),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.customer'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.tax'),
        ),
        migrations.AlterField(
            model_name='transfermoney',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='money_transfer_user', to='organization.customer'),
        ),
    ]
