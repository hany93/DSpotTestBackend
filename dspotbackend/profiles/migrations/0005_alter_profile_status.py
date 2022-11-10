# Generated by Django 4.1.2 on 2022-11-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profilephoto_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.IntegerField(choices=[(0, 'Developing something amazing'), (1, 'This could be interesting....'), (2, 'Man, life is so good'), (3, 'There is nothing quite like a good friend'), (4, 'Take a look around you, everything is awesome'), (5, 'What is the point of all of this'), (6, 'At Work'), (7, 'Hangout out by the pool'), (8, 'At NG Conf!'), (9, 'Designing beatiful things')], default=0),
        ),
    ]
