# Generated by Django 4.0.2 on 2022-02-25 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_category_options_rename_generic_category_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('name', 'strength_name')},
        ),
    ]
