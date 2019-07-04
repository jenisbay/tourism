# Generated by Django 2.2.1 on 2019-07-01 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderer', models.CharField(max_length=500)),
                ('date_ordered', models.DateField()),
                ('date_expired', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupied_rooms', models.PositiveIntegerField(default=0)),
                ('available_rooms', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='photo',
            new_name='image',
        ),
        migrations.AddField(
            model_name='hotel',
            name='services',
            field=models.TextField(default='{}'),
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms_images', to='hotels.Hotel'),
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.AddField(
            model_name='registrationbook',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registration_book', to='hotels.Hotel'),
        ),
        migrations.AddField(
            model_name='booking',
            name='registration_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='hotels.RegistrationBook'),
        ),
    ]