
from django.db    import models
from django.utils import timezone




class Patient (models.Model) :

    def __str__ (self) :
        return self.full_name

    fiscal_code = models.CharField (max_length = 16, primary_key = True)

    full_name   = models.CharField (max_length = 100)



class Allergen (models.Model) :

    def __str__ (self) :
        return self.name

    name      = models.CharField (max_length = 100, primary_key = True)

    threshold = models.IntegerField (default = 0)



class Report (models.Model) :

    patient = models.ForeignKey (Patient, on_delete = models.CASCADE)

    date    = models.DateField (default = timezone.now)



class AllergyTest (models.Model) :

    def __str__ (self) :
        return "%s: %s" % (self.allergen, self.value)

    report   = models.ForeignKey (Report, on_delete = models.CASCADE)

    allergen = models.ForeignKey (Allergen, on_delete = models.CASCADE)

    value    = models.IntegerField ()

