# Generated by Django 3.2.9 on 2022-02-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_auto_20220210_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='forehand',
            field=models.CharField(default='등록전', max_length=20, verbose_name='포핸드사용손'),
        ),
    ]