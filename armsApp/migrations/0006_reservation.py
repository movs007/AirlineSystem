# Generated by Django 4.0.3 on 2022-04-27 07:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('armsApp', '0005_alter_flights_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'Business Class'), ('2', 'Economy')], default='2', max_length=50)),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('email', models.CharField(max_length=250)),
                ('contact', models.CharField(max_length=250)),
                ('address', models.TextField()),
                ('status', models.CharField(choices=[('0', 'Pending'), ('1', 'Confirmed'), ('2', 'Cancelled')], default=0, max_length=2)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armsApp.flights')),
            ],
            options={
                'verbose_name_plural': 'List of Reservations',
            },
        ),
    ]
