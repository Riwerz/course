# Generated by Django 2.1.1 on 2018-10-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rootApp', '0003_auto_20181003_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conspect',
            name='subject',
            field=models.IntegerField(choices=[(0, 'МАТЕМАТИКА'), (1, 'ФИЗИКА'), (2, 'ИСТОРИЯ'), (3, 'ХИМИЯ'), (4, 'БИОЛОГИЯ'), (5, 'ИНФОРМАТИКА'), (6, 'ЛИНГВИСТИКА'), (7, 'ЭКОНОМИКА')], default=0),
        ),
    ]