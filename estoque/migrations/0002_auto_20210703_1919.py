# Generated by Django 3.2.4 on 2021-07-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='nome',
            field=models.CharField(default='produto ', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(),
        ),
    ]
