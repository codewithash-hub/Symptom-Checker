# Generated by Django 5.1.2 on 2024-10-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_checker', '0003_alter_interaction_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
    ]
