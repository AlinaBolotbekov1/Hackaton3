# Generated by Django 4.2.4 on 2023-08-31 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('air_name', models.CharField(max_length=30)),
                ('model_air', models.CharField(max_length=30)),
                ('seats', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_num', models.CharField(max_length=30, verbose_name='Номер рейса')),
                ('origin', models.CharField(max_length=50, verbose_name='Откуда')),
                ('destination', models.CharField(max_length=100, verbose_name='Куда')),
                ('departure_date', models.DateField(verbose_name='Дата вылета')),
                ('departure_time', models.TimeField(verbose_name='Времы вылета')),
                ('arrival_date', models.DateField(verbose_name='Дата прилета')),
                ('arrival_time', models.TimeField(verbose_name='Время прилета')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveIntegerField(verbose_name='Ряд')),
                ('seat_num', models.PositiveIntegerField(verbose_name='Номер места')),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.airplane')),
            ],
        ),
    ]
