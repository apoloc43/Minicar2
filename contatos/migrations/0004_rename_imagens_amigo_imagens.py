# Generated by Django 4.2.5 on 2023-10-10 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0003_remove_amigo_avatar_remove_amigo_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amigo',
            old_name='Imagens',
            new_name='imagens',
        ),
    ]