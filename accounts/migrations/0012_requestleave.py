# Generated by Django 3.1.1 on 2022-11-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLeave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_email', models.EmailField(max_length=254)),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_leaveDateStart', models.DateField()),
                ('emp_leaveDateEnd', models.DateField()),
                ('typeOf_leave', models.CharField(choices=[('Vacation Leave', 'Vacation Leave'), ('Sick Leave', 'Sick Leave')], max_length=50)),
                ('reasonFor_leave', models.CharField(max_length=100)),
                ('IsApproved', models.BooleanField(default=False)),
            ],
        ),
    ]
