from django.db import models

# Create your models here.


class Room(models.Model):
    title = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    seat = models.IntegerField(null=False)
    deskription = models.CharField(max_length=65, null=True, blank=True)
    picture = models.ImageField(null=True)  # upload_to=None

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Комнаты'
        verbose_name = 'Комната'


class Booking(models.Model):
    room = models.ForeignKey('Room', null=None, on_delete=models.PROTECT)
    start_date = models.DateField(null=False, auto_now_add=False)
    end_date = models.DateField(null=False, auto_now_add=False)
    user_name = models.CharField(max_length=50, null=False, default=None)


    def __str__(self):
        return str(self.room)

    class Meta:
        verbose_name_plural = 'Бронирования'
        verbose_name = 'Бронирование'
