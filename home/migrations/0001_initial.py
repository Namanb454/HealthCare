# Generated by Django 4.0.6 on 2023-02-11 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('confirmpassword', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
