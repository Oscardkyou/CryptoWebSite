from django.db import models

class Currency(models.Model):
    title = models.CharField(max_length=300, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")


    def __str__(self):
        return self.title
