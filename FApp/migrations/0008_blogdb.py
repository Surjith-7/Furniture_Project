# Generated by Django 5.1.1 on 2024-10-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FApp', '0007_productdb_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blogimage', models.ImageField(blank=True, null=True, upload_to='blogimage')),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
