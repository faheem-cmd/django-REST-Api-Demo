# Generated by Django 2.2.14 on 2021-09-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=10)),
                ('emp_id', models.IntegerField()),
            ],
        ),
    ]
