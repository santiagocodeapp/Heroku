# Generated by Django 4.0.3 on 2022-03-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyReport', '0003_alter_players_player_positions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='player_positions',
            field=models.ManyToManyField(blank=True, related_name='positions', to='MyReport.positions'),
        ),
    ]