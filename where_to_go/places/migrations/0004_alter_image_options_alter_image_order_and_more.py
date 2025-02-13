# Generated by Django 4.2.17 on 2025-01-16 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order'], 'verbose_name': 'картинка', 'verbose_name_plural': 'картинки'},
        ),
        migrations.AlterField(
            model_name='image',
            name='order',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='places.place', verbose_name='Локация'),
        ),
    ]
