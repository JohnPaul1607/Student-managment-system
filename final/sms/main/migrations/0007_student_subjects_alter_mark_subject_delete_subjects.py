# Generated by Django 4.1.7 on 2023-04-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_subjects_remove_student_english_remove_student_maths_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Subjects',
        ),
    ]
