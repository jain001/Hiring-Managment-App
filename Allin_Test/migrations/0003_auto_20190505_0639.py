# Generated by Django 2.2 on 2019-05-05 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Allin_Test', '0002_questions_solution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='Questions',
            new_name='questions',
        ),
    ]
