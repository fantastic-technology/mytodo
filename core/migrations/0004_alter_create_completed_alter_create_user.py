# Generated by Django 5.0.6 on 2024-09-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_create_user_alter_create_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='create',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
