# Generated by Django 3.1.2 on 2020-10-21 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0007_auto_20201022_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.category'),
        ),
    ]
