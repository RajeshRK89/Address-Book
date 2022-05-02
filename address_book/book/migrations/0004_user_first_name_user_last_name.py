# Generated by Django 4.0.4 on 2022-05-02 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default='na', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
