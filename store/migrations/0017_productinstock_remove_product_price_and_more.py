# Generated by Django 4.0.5 on 2022-06-08 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.FloatField()),
                ('price', models.FloatField()),
                ('sell_price', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Products From Stock',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sell_price',
        ),
        migrations.AlterField(
            model_name='product',
            name='countInStock',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.productinstock'),
        ),
    ]
