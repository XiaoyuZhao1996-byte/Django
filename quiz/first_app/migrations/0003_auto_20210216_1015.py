# Generated by Django 3.1.4 on 2021-02-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_question_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Draft'), (1, 'Voting'), (2, 'End'), (3, 'Deleted')], default=0),
        ),
    ]