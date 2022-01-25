# Generated by Django 3.2.9 on 2022-01-25 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('racket', '0007_remove_racket_visitorreviewscore'),
        ('visitor', '0002_alter_visitorreview_visitorracket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorreview',
            name='visitorRacket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racket.racket'),
        ),
    ]
