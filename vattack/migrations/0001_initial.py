# Generated by Django 3.1.5 on 2021-01-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('e_id', models.EmailField(max_length=254)),
                ('passw', models.CharField(max_length=564)),
                ('c_passw', models.CharField(max_length=556)),
            ],
        ),
    ]
