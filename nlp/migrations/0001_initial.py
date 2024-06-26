# Generated by Django 4.2.10 on 2024-02-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRecommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('website_url', models.URLField()),
                ('google_search_query', models.CharField(max_length=250)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_page_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
