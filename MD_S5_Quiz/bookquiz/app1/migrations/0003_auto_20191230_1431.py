# Generated by Django 2.2 on 2019-12-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20191230_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='wirter',
            field=models.ManyToManyField(related_name='books', related_query_name='bookss', to='app1.Writer'),
        ),
    ]
