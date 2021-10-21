# Generated by Django 3.2.6 on 2021-08-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0007_alter_product_url_externo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('em_destaque',)},
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
