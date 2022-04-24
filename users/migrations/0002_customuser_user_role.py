# Generated by Django 4.0.4 on 2022-04-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_role',
            field=models.CharField(choices=[('Подписчик', 'Подписчик'), ('Автор', 'Автор')], default='Подписчик', editable=False, max_length=10),
            preserve_default=False,
        ),
    ]