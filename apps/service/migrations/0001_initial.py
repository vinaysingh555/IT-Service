# Generated by Django 2.2.7 on 2024-07-26 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('payment_terms', models.CharField(max_length=100)),
                ('service_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('service_package', models.CharField(max_length=100)),
                ('service_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('service_image', models.ImageField(upload_to='services/')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
