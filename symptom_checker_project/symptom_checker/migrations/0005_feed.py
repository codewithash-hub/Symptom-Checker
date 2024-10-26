# Generated by Django 5.1.2 on 2024-10-26 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptom_checker', '0004_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('images', models.ImageField(upload_to='uploads/product/')),
            ],
        ),
    ]
