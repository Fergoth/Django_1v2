# Generated by Django 4.2.17 on 2025-01-16 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('order', models.CharField(choices=[('1', 'Первая'), ('2', 'Вторая')], default='2', max_length=1)),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.place', verbose_name='Локация')),
            ],
        ),
    ]
