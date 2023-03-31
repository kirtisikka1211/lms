# Generated by Django 4.1.5 on 2023-03-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0007_rename_mentee_members_mentee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='end_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='members',
            name='reason',
            field=models.TextField(default='NULL'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='members',
            name='start_date',
            field=models.DateTimeField(null=True),
        ),
    ]