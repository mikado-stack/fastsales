# Generated by Django 3.2.6 on 2022-08-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20220803_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('unlike', 'unlike'), ('like', 'like')], default='like', max_length=10),
        ),
    ]
