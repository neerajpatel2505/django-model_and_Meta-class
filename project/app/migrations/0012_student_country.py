# Generated by Django 5.0.3 on 2024-04-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_student_options_alter_student_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Country',
            field=models.CharField(choices=[('ind', 'india'), ('CA', 'Canada'), ('MX', 'Mexico')], max_length=100, null=True),
        ),
    ]
