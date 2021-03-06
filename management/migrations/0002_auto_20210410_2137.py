# Generated by Django 3.2 on 2021-04-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='contact',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='gender',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='operation',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='operation',
            name='type',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='platform',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='platform',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Web Client'), (0, 'Android'), (0, 'Iphone/Ipad')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='target_age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='target_gender',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='age',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='gender',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
