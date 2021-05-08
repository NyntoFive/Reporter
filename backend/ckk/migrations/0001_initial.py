# Generated by Django 3.2 on 2021-04-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CKKItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=255)),
                ('all_images', models.TextField()),
                ('cannonical_url', models.URLField(blank=True, max_length=255)),
                ('video_url', models.URLField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('link', models.URLField(blank=True, max_length=255)),
                ('products_id', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('discount_tiers', models.CharField(blank=True, max_length=255)),
                ('discount_amount', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]