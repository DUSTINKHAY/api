# Generated by Django 4.1 on 2022-08-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image_u',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('title', models.CharField(max_length=50, null=True)),
                ('product_description', models.CharField(max_length=200, null=True)),
                ('price', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
