# Generated by Django 3.2.9 on 2021-12-06 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_auto_20211205_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pais',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
