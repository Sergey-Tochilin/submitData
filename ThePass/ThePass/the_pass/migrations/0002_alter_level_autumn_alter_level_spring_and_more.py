# Generated by Django 5.0.6 on 2024-05-25 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('the_pass', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='autumn',
            field=models.CharField(choices=[('2Б', '2Б'), ('1Б', '1Б'), ('3А', '3А'), ('3Б', '3Б'), ('2А', '2А'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Осень'),
        ),
        migrations.AlterField(
            model_name='level',
            name='spring',
            field=models.CharField(choices=[('2Б', '2Б'), ('1Б', '1Б'), ('3А', '3А'), ('3Б', '3Б'), ('2А', '2А'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Весна'),
        ),
        migrations.AlterField(
            model_name='level',
            name='summer',
            field=models.CharField(choices=[('2Б', '2Б'), ('1Б', '1Б'), ('3А', '3А'), ('3Б', '3Б'), ('2А', '2А'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Лето'),
        ),
        migrations.AlterField(
            model_name='level',
            name='winter',
            field=models.CharField(choices=[('2Б', '2Б'), ('1Б', '1Б'), ('3А', '3А'), ('3Б', '3Б'), ('2А', '2А'), ('1А', '1А')], default='1А', max_length=2, verbose_name='Зима'),
        ),
        migrations.AlterField(
            model_name='pereval',
            name='status',
            field=models.CharField(choices=[('PN', 'в работе'), ('AC', 'принят'), ('RJ', 'отклонён'), ('NW', 'новый')], default='NW', max_length=2),
        ),
    ]