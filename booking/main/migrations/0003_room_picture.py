# Generated by Django 4.1.7 on 2023-03-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_room_deskription'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
