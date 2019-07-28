# Generated by Django 2.2.1 on 2019-05-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professors', '0006_auto_20190521_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='title',
            field=models.CharField(default='professor', max_length=124),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='professor',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]