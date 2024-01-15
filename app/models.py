from django.db import models
from django.contrib.auth.models import User

    
class Habitat(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "A", "действует"
        DELETED = "D", "удален"
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ACTIVE, verbose_name="Статус") # статус удален/действует

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="Название места обитания")
    desc = models.CharField(max_length=1000, verbose_name="Описание места обитания")

    class Environment(models.TextChoices):
        AIR_GROUND = "AG", "наземно-воздушная"
        WATER = "W", "водная"
        SOIL = "S", "почвенная"
    env = models.CharField(max_length=2, choices=Environment.choices, default=Environment.AIR_GROUND, verbose_name="Среда")

    class Origin(models.TextChoices):
        BIO = "B", "биогенная"
        ART = "A", "антропогенная" #artifitial
    origin = models.CharField(max_length=1, choices=Origin.choices, default=Origin.BIO, verbose_name="Происхождение") 
     # биогенное или антропогенное

    image = models.CharField(max_length=50) 

    def __str__(self):
        return f'{self.title}'

class Animal(models.Model):

    class Status(models.TextChoices):
        ENTERED = "E", "введён"
        ACTIVE = "A", "в работе"
        FINISHED = "F", "завершён"
        CANCELLED = "C", "отменён"
        DELETED = "D", "удалён"

    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ENTERED, verbose_name="Статус заявки") # введён, в работе, завершён, отменён, удалён

    id = models.IntegerField(primary_key=True)

    genus_lat = models.CharField(max_length=50, verbose_name="Род лат.", default="Homo") # род
    genus_rus = models.CharField(max_length=50, verbose_name="Род рус. (опц.) ", null=True) # род
    species_lat = models.CharField(max_length=50, verbose_name="Вид лат.", default="Sapiens") # вид
    species_rus = models.CharField(max_length=50, verbose_name="Вид рус. (опц.) ", null=True)
    family_lat = models.CharField(max_length=50, verbose_name="Семейство лат. (опц.) ", null=True) # семейство
    family_rus = models.CharField(max_length=50, verbose_name="Семейство рус. (опц.) ", null=True)
    # даты начала и завершения заявки
    start_date = models.DateField(auto_now=True, null=True, verbose_name="Начало заявки")
    fin_date = models.DateField(blank=True, null=True, verbose_name="Завершение заявки")  

    creator = models.ForeignKey(User, models.CASCADE, related_name='creator', verbose_name="Создатель заявки", null=True)
    moderator = models.ForeignKey(User, models.CASCADE, related_name='moderator', verbose_name="Модератор заявки", null=True)

    image = models.CharField(max_length=50) 

    def __str__(self):
        return f'{self.genus_lat} {self.species_lat}'


class HabitatSpecies(models.Model):
    id = models.IntegerField(primary_key=True)

    habitat = models.ForeignKey(Habitat, models.CASCADE)
    species = models.ForeignKey(Animal, models.CASCADE)

    class Meta:
        unique_together = ('habitat', 'species')


