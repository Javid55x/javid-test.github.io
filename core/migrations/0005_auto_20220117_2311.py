# Generated by Django 3.2.7 on 2022-01-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_product_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-date',)},
        ),
    ]
