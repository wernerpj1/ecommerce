# Generated by Django 3.2.6 on 2021-09-04 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0008_auto_20210812_1102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-em_destaque',)},
        ),
    ]