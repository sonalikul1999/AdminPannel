# Generated by Django 2.1.1 on 2020-04-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='id',
        ),
        migrations.RemoveField(
            model_name='vendorsdata',
            name='Vendor_ID',
        ),
        migrations.AlterField(
            model_name='userdata',
            name='User_Email',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]