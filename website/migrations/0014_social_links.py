# Generated by Django 5.0 on 2024-09-12 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_delete_social_links'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True)),
                ('calendely', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]