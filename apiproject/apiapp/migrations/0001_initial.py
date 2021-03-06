# Generated by Django 3.1.2 on 2022-01-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.IntegerField()),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('companyname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('web', models.CharField(max_length=200)),
            ],
        ),
    ]
