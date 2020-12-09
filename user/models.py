from django.db import models


class Modell(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Images(models.Model):
    Profile = (
        ('научный', 'научный'),
        ('историчекский', 'историчекский'),
    )
    With = (
        ('друг', 'друзья'),
        ('семь' or 'семей', 'семья'),
        ('реб' or 'дет', 'дети'),
    )
    Price = (
        ('дёшево', 'от 100-299'),
        ('дорого', 'от 300'),
    )
    Time = (
        ('утро', '06:00-11:59'),
        ('день', '12:00-17:99'),
        ('вечер', '18:00-23:99'),
    )
    name = models.CharField(max_length=150)
    image = models.ImageField("Изображение", upload_to="image/")
    profile = models.CharField("Профиль",
                               max_length=100,
                               choices=Profile,
                               )
    wth = models.CharField("С кем-то",
                           max_length=100,
                           choices=With,
                           )
    price = models.CharField("Цена",
                             max_length=100,
                             choices=Price,
                             )
    time = models.CharField("Время",
                            max_length=100,
                            choices=Time,
                            )

    def __str__(self):
        return self.name
