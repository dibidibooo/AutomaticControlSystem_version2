<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-04-14 13:00
=======
# Generated by Django 4.0.3 on 2022-04-14 17:40
>>>>>>> d30fb895622580ee981ab6c5f84a1468a43c564b

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_comment_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления'),
        ),
    ]
