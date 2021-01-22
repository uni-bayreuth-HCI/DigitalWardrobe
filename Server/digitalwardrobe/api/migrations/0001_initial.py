# Generated by Django 3.0.5 on 2021-01-17 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('r_type', models.CharField(default='', max_length=100)),
                ('weather', models.CharField(default='all', max_length=100)),
            ],
        ),
    ]