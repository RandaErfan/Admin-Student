# Generated by Django 3.2.20 on 2023-10-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20231007_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='student_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
