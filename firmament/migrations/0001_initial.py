# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField()),
                ('last_page_number', models.IntegerField(blank=True, null=True)),
                ('short_name', models.CharField(max_length=1024)),
                ('year', models.IntegerField()),
                ('manuscript', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Proof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('docx', models.FileField(blank=True, null=True, upload_to='')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='')),
                ('pdf_status', models.CharField(blank=True, choices=[('pending', 'pending'), ('generated', 'generated'), ('failed', 'failed')], default='pending', max_length=10, null=True)),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_number', models.IntegerField()),
                ('back_matter_proofs', models.ManyToManyField(related_name='back_matter_volumes', to='firmament.Proof')),
                ('front_matter_proofs', models.ManyToManyField(related_name='front_matter_volumes', to='firmament.Proof')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='firmament.Series')),
            ],
        ),
        migrations.AddField(
            model_name='case',
            name='proofs',
            field=models.ManyToManyField(related_name='cases', to='firmament.Proof'),
        ),
        migrations.AddField(
            model_name='case',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='firmament.Volume'),
        ),
    ]
