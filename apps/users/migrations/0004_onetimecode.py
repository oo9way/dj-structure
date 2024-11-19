# Generated by Django 5.1.3 on 2024-11-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_phone_numnber'),
    ]

    operations = [
        migrations.CreateModel(
            name='OneTimeCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6)),
                ('phone_number', models.CharField(max_length=13)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
