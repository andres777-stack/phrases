# Generated by Django 4.0.4 on 2022-06-09 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phrases', '0007_rename_tag_phrase_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag']},
        ),
    ]
