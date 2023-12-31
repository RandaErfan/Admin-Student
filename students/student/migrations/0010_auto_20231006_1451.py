# Generated by Django 3.2.20 on 2023-10-06 12:51

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='borrowed_by',
        ),
        migrations.AddField(
            model_name='borrow',
            name='student_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.IntegerField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(default=student.models.get_return_date),
        ),
    ]
