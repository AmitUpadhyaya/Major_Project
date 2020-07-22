# Generated by Django 2.1.5 on 2020-07-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('name', models.CharField(max_length=50)),
                ('cuisine', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Restaurants',
            },
        ),
    ]
