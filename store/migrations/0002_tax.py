# Generated by Django 3.2.6 on 2022-06-08 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
