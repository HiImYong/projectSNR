# Generated by Django 3.2.9 on 2022-02-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('racket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='racket',
            name='visitorAvgScore',
            field=models.FloatField(default=0, verbose_name='사용자평점평균'),
        ),
        migrations.AlterField(
            model_name='racketdetail',
            name='adminAvgScore',
            field=models.FloatField(default=0, verbose_name='운영자평점평균'),
        ),
    ]
