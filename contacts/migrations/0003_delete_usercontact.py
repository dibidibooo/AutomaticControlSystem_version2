# Generated by Django 4.0.3 on 2022-03-16 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_usercontact_tel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserContact',
        ),
    ]
