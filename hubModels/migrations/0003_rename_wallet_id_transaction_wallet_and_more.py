# Generated by Django 4.1.1 on 2023-04-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubModels', '0002_alter_transaction_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='wallet_id',
            new_name='wallet',
        ),
        migrations.AddField(
            model_name='transaction',
            name='title',
            field=models.CharField(default='Amazong Prime', max_length=200),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]