# Generated by Django 3.2.9 on 2022-02-10 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_player_countlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='playerCharacteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Characteristic', models.CharField(max_length=20, verbose_name='선수특성')),
                ('aboutCharacteristic', models.CharField(max_length=20, verbose_name='선수특성설명')),
            ],
        ),
    ]