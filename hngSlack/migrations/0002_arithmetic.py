# Generated by Django 4.1.2 on 2022-11-04 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hngSlack', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arithmetic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(max_length=90)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
            ],
        ),
    ]
