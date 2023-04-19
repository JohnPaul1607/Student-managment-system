# Generated by Django 4.1.7 on 2023-04-19 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_student_subjects_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamil', models.CharField(max_length=100, null=True)),
                ('english', models.CharField(max_length=100, null=True)),
                ('maths', models.CharField(max_length=100, null=True)),
                ('science', models.CharField(max_length=100, null=True)),
                ('social', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='english',
        ),
        migrations.RemoveField(
            model_name='student',
            name='maths',
        ),
        migrations.RemoveField(
            model_name='student',
            name='science',
        ),
        migrations.RemoveField(
            model_name='student',
            name='social',
        ),
        migrations.RemoveField(
            model_name='student',
            name='tamil',
        ),
        migrations.AlterField(
            model_name='mark',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subjects'),
        ),
    ]
