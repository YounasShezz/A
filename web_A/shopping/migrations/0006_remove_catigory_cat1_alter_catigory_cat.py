# Generated by Django 5.0 on 2024-01-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_alter_prodect_contity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catigory',
            name='cat1',
        ),
        migrations.AlterField(
            model_name='catigory',
            name='cat',
            field=models.CharField(blank=True, choices=[('kjlf', 'kjlf'), ('kjlfdfsg', 'kjlfdfsg'), ('خضر', 'خضر')], max_length=40),
        ),
    ]