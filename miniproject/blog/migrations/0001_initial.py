# Generated by Django 4.2 on 2023-04-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year_of_brith', models.DateTimeField()),
                ('Year_of_death', models.DateTimeField(blank=True)),
                ('type_of_activity', models.TextField()),
                ('Reason_for_popularity', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
