# Generated by Django 4.2.5 on 2023-09-05 15:01
# создается через терминал пишем makemigrations и ентер, также можно редактировать вручную

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp', models.CharField(max_length=10)),
                ('manufacturer', models.CharField(max_length=10)),
                ('release_date', models.IntegerField()),
                ('state_number', models.CharField(max_length=10)),
            ],
        ),
    ]
