# Generated by Django 3.1.2 on 2020-10-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('optiona', models.CharField(max_length=100)),
                ('optionb', models.CharField(max_length=100)),
                ('optionc', models.CharField(max_length=100)),
                ('optiond', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('catagory', models.CharField(choices=[('set1', 'Set1'), ('set2', 'Set2'), ('set3', 'Set3'), ('set4', 'Set4')], max_length=20)),
            ],
            options={
                'ordering': ('-catagory',),
            },
        ),
    ]
