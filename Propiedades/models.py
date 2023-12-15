from django.db import models

# Create your models here.
class Property(models.Model):
    #Definimos variables para elegir más adelante.
    HOUSE = "HOS"
    APARTMENT = "APM"
    MANSION = "MAN"
    DUPLEX = "DUP"
    STUDY = "STU"
    #Definimos las opciones para el tipo de propiedad
    TIPO_PROPIEDADES = {
        (HOUSE, "House"),
        (APARTMENT, "Apartment"),
        (MANSION, "Mansion"),
        (DUPLEX, "Duplex"),
        (STUDY, "Study"),
    }

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=TIPO_PROPIEDADES, default='Apartment')
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_feet = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title