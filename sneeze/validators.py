
from django.core.exceptions import ValidationError

import codicefiscale




def validate_fiscal_code (fiscal_code) :
    if codicefiscale.isvalid (fiscal_code) :
        return None
    else :
        raise ValidationError ("Please enter a valid fiscal code.")

