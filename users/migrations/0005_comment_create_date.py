# Generated by Django 4.1.1 on 2022-11-05 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]