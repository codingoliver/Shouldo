# Generated by Django 2.2.6 on 2019-10-06 15:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
                ('due_date', models.DateField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2019, 10, 6, 15, 36, 43, 865106, tzinfo=utc), editable=False)),
                ('updated_date', models.DateTimeField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
