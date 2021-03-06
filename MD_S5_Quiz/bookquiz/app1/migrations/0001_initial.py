# Generated by Django 2.2 on 2019-12-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('chap', models.DateField()),
                ('inter_exter', models.BooleanField()),
                ('translator', models.CharField(blank=True, max_length=200)),
                ('wirter', models.ManyToManyField(to='app1.Writer')),
            ],
        ),
    ]
