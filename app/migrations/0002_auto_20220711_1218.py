# Generated by Django 3.1.6 on 2022-07-11 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='voiture',
            name='marque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.marque'),
        ),
    ]
