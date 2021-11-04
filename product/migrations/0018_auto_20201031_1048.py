# Generated by Django 3.1.1 on 2020-10-31 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20201031_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankinfo',
            name='name',
        ),
        migrations.AddField(
            model_name='bankinfo',
            name='account_name',
            field=models.CharField(default='talha', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bankinfo',
            name='bank_name',
            field=models.CharField(default='dbbl', max_length=50),
            preserve_default=False,
        ),
    ]