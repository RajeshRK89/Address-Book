# Generated by Django 4.0.4 on 2022-05-02 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='name')),
                ('last', models.PositiveIntegerField(verbose_name='last value')),
            ],
            options={
                'verbose_name': 'sequence',
                'verbose_name_plural': 'sequences',
            },
        ),
    ]