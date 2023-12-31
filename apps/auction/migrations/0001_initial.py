# Generated by Django 5.0 on 2024-01-02 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('PENDING', 'pending'), ('OPEN', 'open'), ('CLOSED', 'closed'), ('CANCELLED', 'cancelled')], default='pending', max_length=20, verbose_name='status')),
            ],
            options={
                'verbose_name': 'auction',
                'verbose_name_plural': 'auctions',
                'db_table': 'auction',
            },
        ),
    ]
