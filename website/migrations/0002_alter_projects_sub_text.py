# Generated by Django 5.0 on 2024-02-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='sub_text',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
