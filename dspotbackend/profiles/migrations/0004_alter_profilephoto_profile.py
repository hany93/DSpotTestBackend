# Generated by Django 4.1.2 on 2022-11-06 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilephoto',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profilephotos', to='profiles.profile'),
        ),
    ]