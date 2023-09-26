from django.db import models
from django.contrib.auth.models import User


class Profile(User):
    avatar = models.ImageField()

    def __str__(self):
        return f'{self.username}'
    
class Habitat(models.Model):
    status = models.CharField(max_length=50) # статус удален/действует

    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100) 
    env = models.CharField(max_length=50)  # водная, наземно-воздушная, почвенная, организменная
    origin = models.CharField(max_length=50)  # биогенное или антропогенное
    countries = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return f'{self.title}'

class Animal(models.Model):
    status = models.CharField(max_length=50) # введён, в работе, завершён, отменён, удалён

    id = models.IntegerField(primary_key=True)
    genus = models.CharField(max_length=50) # род
    species = models.CharField(max_length=50) # вид
    family = models.CharField(max_length=50) # семейство
    start_date = models.DateField(blank=True, null=True)
    fin_date = models.DateField(blank=True, null=True)  
    moderator = models.ForeignKey(Profile, models.CASCADE)
    image = models.ImageField() 

    def __str__(self):
        return f'{self.genus} {self.species}'


class HabitatSpecies(models.Model):
    id = models.IntegerField(primary_key=True)

    habitat = models.ForeignKey(Habitat, models.CASCADE)
    species = models.ForeignKey(Animal, models.CASCADE)

    class Meta:
        unique_together = ('habitat', 'species')


