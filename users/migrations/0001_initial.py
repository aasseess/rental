# Generated by Django 4.0.3 on 2022-04-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('role', models.CharField(choices=[('Rider', 'Rider'), ('Provider', 'Provider')], default='Rider', max_length=10)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hires_in_progress', models.IntegerField(default=0)),
                ('wallet_balance', models.FloatField(default=0.0)),
                ('amount_owed', models.FloatField(default=0.0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
