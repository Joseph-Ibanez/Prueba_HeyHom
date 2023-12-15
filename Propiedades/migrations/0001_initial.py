# Generated by Django 5.0 on 2023-12-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=255)),
                ('property_type', models.CharField(choices=[('MAN', 'Mansion'), ('STU', 'Study'), ('HOS', 'House'), ('APM', 'Apartment'), ('DUP', 'Duplex')], default='Apartment', max_length=20)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('square_feet', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
