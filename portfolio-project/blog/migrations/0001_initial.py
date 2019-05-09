# Generated by Django 2.1.3 on 2019-04-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.CharField(max_length=10)),
                ('body', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
