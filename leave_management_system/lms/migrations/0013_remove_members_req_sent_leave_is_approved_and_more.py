# Generated by Django 4.1.5 on 2023-04-02 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0012_remove_members_end_date_remove_members_reason_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='req_sent',
        ),
        migrations.AddField(
            model_name='leave',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leave',
            name='is_rejected',
            field=models.BooleanField(default=False),
        ),
    ]
