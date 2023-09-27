from django.db import models
from django.contrib.auth.models import User

    
class Habitat(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "A", "действует"
        DELETED = "D", "удален"
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ACTIVE) # статус удален/действует

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    class Environment(models.TextChoices):
        AIR_GROUND = "AG", "наземно-воздушная"
        WATER = "W", "водная"
        SOIL = "S", "почвенная"
    env = models.CharField(max_length=2, choices=Environment.choices, default=Environment.AIR_GROUND)

    class Origin(models.TextChoices):
        BIO = "B", "биогенная"
        ART = "A", "антропогенная" #artifitial
    origin = models.CharField(max_length=1, choices=Origin.choices, default=Origin.BIO)  # биогенное или антропогенное

    image = models.ImageField(upload_to='img')

    def __str__(self):
        return f'{self.title}'

class Animal(models.Model):

    class Status(models.TextChoices):
        ENTERED = "E", "введён"
        ACTIVE = "A", "в работе"
        FINISHED = "F", "завершён"
        CANCELLED = "C", "отменён"
        DELETED = "D", "удалён"

    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ENTERED) # введён, в работе, завершён, отменён, удалён

    id = models.IntegerField(primary_key=True)

    genus = models.CharField(max_length=50) # род
    species = models.CharField(max_length=50) # вид
    family = models.CharField(max_length=50) # семейство
    # даты начала и завершения заявки
    start_date = models.DateField(auto_now=True, null=True)
    fin_date = models.DateField(blank=True, null=True)  

    moderator = models.ForeignKey(User, models.CASCADE)
    image = models.ImageField(upload_to='img') 

    def __str__(self):
        return f'{self.genus} {self.species}'


class HabitatSpecies(models.Model):
    id = models.IntegerField(primary_key=True)

    habitat = models.ForeignKey(Habitat, models.CASCADE)
    species = models.ForeignKey(Animal, models.CASCADE)

    class Meta:
        unique_together = ('habitat', 'species')


