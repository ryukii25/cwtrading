# Generated by Django 3.1.7 on 2021-03-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covercall', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoverCall1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetPrice', models.DecimalField(decimal_places=10, max_digits=19)),
                ('strikePrice', models.DecimalField(decimal_places=10, max_digits=19)),
                ('maturity', models.DecimalField(decimal_places=10, max_digits=19)),
                ('rate', models.DecimalField(decimal_places=10, max_digits=19)),
                ('volatility', models.DecimalField(decimal_places=10, max_digits=19)),
                ('optionsPrice', models.DecimalField(decimal_places=10, max_digits=19)),
                ('numberStock', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='closePrice',
            new_name='ClosePrice1',
        ),
        migrations.DeleteModel(
            name='coverCall',
        ),
    ]
