# Generated by Django 3.2.23 on 2024-06-24 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CHECKOUT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('productId', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
