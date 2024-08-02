# Generated by Django 4.2.4 on 2024-01-28 11:51

import ckeditor.fields
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('text', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('q', models.CharField(max_length=500)),
                ('a', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('file', models.FileField(blank=True, upload_to='research/pdfs/%Y', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Wrong Extension')])),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, upload_to='research/img/%Y')),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Road',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pub_date', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('home', models.BooleanField(default=False)),
                ('year', models.IntegerField(default=0)),
                ('term', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('cv', models.FileField(blank=True, upload_to='team/pdf/%Y/%m/', validators=[django.core.validators.FileExtensionValidator(['pdf'], 'Wrong extension')])),
                ('biography', models.TextField()),
                ('pic', models.ImageField(blank=True, upload_to='team/pic/%Y/%m/%d')),
                ('contact', models.TextField(blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['add_date'],
            },
        ),
    ]
