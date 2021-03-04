# Generated by Django 3.1.7 on 2021-03-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_animal', models.CharField(choices=[('CAT', 'Кошка'), ('DOG', 'Собака')], default='CAT', max_length=3, verbose_name='Разновидность животного')),
                ('name', models.CharField(max_length=100, verbose_name='Кличка')),
                ('breed', models.CharField(blank=True, max_length=150, null=True, verbose_name='Порода')),
                ('description', models.TextField(null='-', verbose_name='Описание')),
                ('age', models.SmallIntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('receipt_date', models.DateField(verbose_name='Дата поступления')),
                ('gender', models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], default='Мальчик', max_length=7, verbose_name='Пол')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='animals_img', verbose_name='Загрузить фото')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
    ]