# Generated by Django 4.2.9 on 2024-01-22 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
