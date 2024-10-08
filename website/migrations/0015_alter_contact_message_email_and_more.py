# Generated by Django 5.0 on 2024-10-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_social_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_message',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact_message',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact_message',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
    ]
