# Generated by Django 5.1.3 on 2024-12-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TodoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todotimestamp', models.DateTimeField(auto_now_add=True)),
                ('todotitle', models.CharField(max_length=100)),
                ('tododescription', models.CharField(max_length=1000)),
                ('tododate', models.DateField()),
                ('todostatus', models.CharField(choices=[('OPEN', 'OPEN'), ('WORKING', 'WORKING'), ('PENDING REVIEW', 'PENDING REVIEW'), ('COMPLETED', 'COMPLETED'), ('OVERDUE', 'OVERDUE'), ('CANCELLED', 'CANCELLED')], max_length=1000)),
                ('todotag', models.ManyToManyField(blank=True, to='Todo.tag')),
            ],
        ),
    ]
