# Generated by Django 2.2.1 on 2019-05-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0008_auto_20190522_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='professor',
            name='communication',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='professor',
            name='marking',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='professor',
            name='objectivity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='professor',
            name='quality',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='professor',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]