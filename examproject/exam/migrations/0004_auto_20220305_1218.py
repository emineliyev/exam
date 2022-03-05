# Generated by Django 3.2.12 on 2022-03-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20220305_1215'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='foreignlanguage',
            options={'ordering': ['title'], 'verbose_name': 'Xarici dil', 'verbose_name_plural': 'Xarici dil'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'ordering': ['title'], 'verbose_name': 'Cins', 'verbose_name_plural': 'Cins'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title'], 'verbose_name': 'Qrup', 'verbose_name_plural': 'Qrup'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['title'], 'verbose_name': 'Bölmə', 'verbose_name_plural': 'Bölmə'},
        ),
        migrations.AlterField(
            model_name='foreignlanguage',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Xarici dil'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Cins'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Bölmə'),
        ),
    ]
