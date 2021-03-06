# Generated by Django 4.0.5 on 2022-06-09 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuadraticEquationSolving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(null=True, verbose_name="Coefficient 'a'")),
                ('b', models.FloatField(null=True, verbose_name="Coefficient 'b'")),
                ('c', models.FloatField(null=True, verbose_name="Coefficient 'c'")),
                ('discriminant', models.FloatField(default=None, null=True, verbose_name='Discriminant')),
                ('solution_1', models.FloatField(default=None, null=True, verbose_name='The first root of the equation `X1`')),
                ('solution_2', models.FloatField(default=None, null=True, verbose_name='The first root of the equation `X2`')),
            ],
            options={
                'verbose_name': 'Solving the quadratic equation',
                'verbose_name_plural': 'Solutions of quadratic equations',
                'ordering': ('solution_1', 'solution_2'),
                'unique_together': {('a', 'b', 'c')},
            },
        ),
    ]
