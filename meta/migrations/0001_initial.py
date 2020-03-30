# Generated by Django 3.0.4 on 2020-03-30 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('creator', models.CharField(max_length=1000)),
            ],
            options={
                'unique_together': {('name', 'creator')},
            },
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeric_column', models.CharField(max_length=500)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.Table')),
            ],
            options={
                'unique_together': {('table', 'numeric_column')},
            },
        ),
    ]
