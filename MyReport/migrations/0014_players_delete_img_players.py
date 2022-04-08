# Generated by Django 4.0.3 on 2022-03-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyReport', '0013_img_players_delete_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=64)),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('player_positions', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='IMG_Players',
        ),
    ]