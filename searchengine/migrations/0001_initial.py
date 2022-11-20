# Generated by Django 4.1.2 on 2022-11-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('Hotel_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('hotelname', models.TextField(max_length=30)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hotelstars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('Hotel_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('depatureDate', models.DateTimeField()),
                ('returnDate', models.DateTimeField()),
                ('countAdults', models.IntegerField()),
                ('countChildren', models.IntegerField()),
                ('price', models.IntegerField()),
                ('inbounddepartureairport', models.TextField(max_length=3)),
                ('inboundarrivalairport', models.TextField(max_length=3)),
                ('inboundairline', models.TextField(max_length=3)),
                ('inboundarrivaldatetime', models.DateTimeField()),
                ('outbounddepartureairport', models.TextField(max_length=3)),
                ('outboundarrivalairport', models.TextField(max_length=3)),
                ('outboundairline', models.TextField(max_length=3)),
                ('outboundarrivaldatetime', models.DateTimeField()),
                ('mealtype', models.TextField(max_length=9)),
                ('oceanview', models.BooleanField()),
                ('roomtype', models.TextField(max_length=11)),
            ],
        ),
    ]
