# Generated by Django 3.2.6 on 2021-10-07 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assistencia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sugestao',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrdemServico',
        ),
        migrations.DeleteModel(
            name='Sugestao',
        ),
    ]