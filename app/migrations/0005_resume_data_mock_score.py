# Generated by Django 5.0.1 on 2024-02-22 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_resume_data_intro_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_data',
            name='mock_score',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
