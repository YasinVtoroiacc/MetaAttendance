# Generated by Django 5.1.1 on 2024-10-04 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_remove_student_gender_remove_teacher_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='check_in_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='student',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', max_length=20),
        ),
    ]
