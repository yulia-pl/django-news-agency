# Generated by Django 4.1 on 2024-12-09 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newspapers', '0002_redactor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspapers.topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Redactor',
        ),
    ]