# Generated by Django 4.0.4 on 2022-04-29 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_booking_return_time_booking_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='vehicles/')),
            ],
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='image',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='images',
            field=models.ManyToManyField(blank=True, default=None, related_name='vehicle_images', to='main.vehicleimage'),
        ),
    ]
