# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_arrival', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='pharmacy',
            fields=[
                ('pharmacy_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pharmacy_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('owner_fname', models.CharField(max_length=50)),
                ('owner_lname', models.CharField(max_length=50)),
                ('vat_no', models.ImageField(upload_to='')),
                ('drug_license', models.ImageField(upload_to='')),
                ('address_street', models.TextField()),
                ('address_city', models.CharField(max_length=20)),
                ('address_state', models.CharField(max_length=20)),
                ('address_pincode', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='notifications',
            name='pharmacy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacy'),
        ),
        migrations.AddField(
            model_name='contact_pharmacy',
            name='pharmacy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacy'),
        ),
    ]
