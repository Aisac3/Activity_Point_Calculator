# Generated by Django 3.2.17 on 2023-10-17 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20231017_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activitylist',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['user']},
        ),
    ]