# Generated by Django 4.0.4 on 2022-06-01 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrases', '0002_phrase_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='slug',
            field=models.SlugField(default='foo', editable=False, unique=True),
            preserve_default=False,
        ),
    ]
