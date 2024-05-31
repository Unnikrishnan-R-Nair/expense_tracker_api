# Generated by Django 5.0.1 on 2024-04-07 10:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Transportation', 'Transportation'), ('House_Rent', 'House_Rent'), ('Water_Bill', 'Water_Bill'), ('Electricity_Bill', 'Electricity_Bill'), ('Hospital_Bill', 'Hospital_Bill'), ('Education', 'Education'), ('Personal_Care', 'Personal_Care'), ('Debt_Payment', 'Dept_Payment'), ('EMI', 'EMI'), ('Entertainment', 'Entertainment'), ('Recharges', 'Recharges'), ('Savings', 'Savings'), ('Miscellaneous', 'Miscellaneous')], default='Miscellaneous', max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('priority', models.CharField(choices=[('need', 'need'), ('want', 'want')], default='need', max_length=50)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Salary', 'Salary'), ('Interest', 'Interest'), ('Business', 'Business'), ('Rental', 'Rental'), ('Agriculture', 'Agriculture'), ('Freelancing', 'Freelancing'), ('Stock_Trading', 'Stock_Trading'), ('Dividend', 'Dividend'), ('Royalty', 'Royalty'), ('Capital', 'Capital'), ('Pension', 'Pension'), ('SocialSecurity', 'SocialSecurity'), ('Other', 'Other')], default='Salary', max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
