# Generated by Django 3.2.20 on 2023-10-03 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='student/images')),
                ('details', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('borrowed_at', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='student.book'),
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
