# Generated by Django 5.1.2 on 2024-10-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('status', models.CharField(max_length=10)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
