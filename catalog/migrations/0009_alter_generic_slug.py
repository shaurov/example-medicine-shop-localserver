# Generated by Django 4.0.2 on 2022-02-25 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generic',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]