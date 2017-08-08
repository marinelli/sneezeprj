
from django  import forms
from .models import Allergen, Patient



class AllergenForm (forms.ModelForm) :
    class Meta :
        model  = Allergen
        fields = ( 'name', 'threshold', )



class PatientForm (forms.ModelForm) :
    class Meta :
        model  = Patient
        fields = ( 'full_name', 'fiscal_code', )

