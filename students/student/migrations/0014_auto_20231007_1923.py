# Generated by Django 3.2.20 on 2023-10-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20231007_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.CharField(max_length=100, null=True),
        ),
    ]