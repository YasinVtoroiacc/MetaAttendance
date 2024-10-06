# Generated by Django 5.1.1 on 2024-10-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0014_remove_profile_gender_alter_attendance_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('late', 'Late'), ('absent', 'Absent')], max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], max_length=100),
        ),
    ]