
from django  import forms
from .models import Allergen, Patient, Report, AllergyTest




class AllergenForm (forms.ModelForm) :
    class Meta :
        model  = Allergen
        fields = ( 'name', 'threshold' )



class PatientForm (forms.ModelForm) :
    class Meta :
        model  = Patient
        fields = ( 'full_name', 'fiscal_code' )



class ReportForm (forms.ModelForm) :
    class Meta :
        model  = Report
        fields = ( 'patient', 'date' )



class AllergyTestForm (forms.ModelForm) :
    class Meta :
        model  = AllergyTest
        fields = ( 'allergen', 'value' )

