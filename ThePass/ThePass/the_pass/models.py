from django.db import models

# Create your models here.

class MyUser(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Телефон')

class Coords(models.Model):
    latitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

class Level(models.Model):
    level_1 = '1А'
    level_2 = '1Б'
    level_3 = '2А'
    level_4 = '2Б'
    level_5 = '3А'
    level_6 = '3Б'

    LEVEL_CHOICES = {
        (level_1, '1А'),
        (level_2, '1Б'),
        (level_3, '2А'),
        (level_4, '2Б'),
        (level_5, '3А'),
        (level_6, '3Б')
    }

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=level_1, verbose_name='Зима')
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=level_1, verbose_name='Весна')
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=level_1, verbose_name='Лето')
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=level_1, verbose_name='Осень')

class Pereval(models.Model):
    status_new = 'new'
    status_pending = 'pending'
    status_accepted = 'accepted'
    status_rejected = 'rejected'

    STATUS_CHOICES = {
        (status_new, 'новый'),
        (status_pending, 'в работе'),
        (status_accepted, 'принят'),
        (status_rejected, 'отклонён')
    }

    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=status_new)
    beauty_name = models.CharField(max_length=255, default='пер.')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_titles = models.CharField(max_length=255, verbose_name='Альтернативное название')
    connect = models.CharField(max_length=500, verbose_name='Что соединяет')
    add_time = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='Автор')
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE, verbose_name='Координаты')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Уровень сложности')

class Image(models.Model):
    data = models.CharField(max_length=2000, verbose_name='ссылка на изображение')
    title = models.CharField(max_length=2000, verbose_name='Описание изображения')

    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, verbose_name='Изображения')






