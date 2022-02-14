# Generated by Django 3.2.9 on 2022-02-14 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0007_playercharacteristic_playerjoin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playercharacteristic',
            name='playerJoin',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Player', to='player.player'),
        ),
    ]
