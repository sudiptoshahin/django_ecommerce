# Generated by Django 4.0.4 on 2022-05-20 18:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('discount_price', models.CharField(blank=True, max_length=100, null=True)),
                ('stock', models.IntegerField()),
                ('color', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('tags', models.ManyToManyField(blank=True, to='product.tag')),
            ],
        ),
    ]
