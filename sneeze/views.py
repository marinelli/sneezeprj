
from django.http            import JsonResponse, Http404
from django.shortcuts       import render
from django.template.loader import render_to_string

from .forms                 import AllergenForm, PatientForm, ReportForm
from .models                import Allergen, Patient, Report, AllergyTest




# manage allergens
#


def allergen_list (request) :

    allergens = Allergen.objects.all ()

    return render (request, 'sneeze/allergen_list.html', {'allergens': allergens})



def save_allergen_form (request, form, template_name) :

    data = dict ()

    if request.method == 'POST' :
        if form.is_valid ():
            form.save ()
            data ['form_is_valid'] = True
            allergens = Allergen.objects.all()
            data ['html_list'] = render_to_string ('sneeze/allergen_list.partial.html', { 'allergens': allergens })
        else :
            data ['form_is_valid'] = False

    context = { 'form': form }
    data ['html_form'] = render_to_string (template_name, context, request = request)

    return JsonResponse (data)



def allergen_create (request) :
    if request.method == 'POST' :
        form = AllergenForm (request.POST)
    else :
        form = AllergenForm ()

    return save_allergen_form (request, form, 'sneeze/allergen_create.partial.html')



def allergen_update (request, pk) :
    try :
        cur_allergen = Allergen.objects.get (pk = pk)
    except Allergen.DoesNotExist :
        raise Http404 ("Allergen does not exist")
    
    if request.method == 'POST' :
        form = AllergenForm (request.POST, instance = cur_allergen)
    else :
        form = AllergenForm (instance = cur_allergen)

    return save_allergen_form (request, form, 'sneeze/allergen_update.partial.html')



def allergen_delete (request, pk) :
    try :
        cur_allergen = Allergen.objects.get (pk = pk)
    except Allergen.DoesNotExist :
        raise Http404 ("Allergen does not exist")

    data = dict ()

    if request.method == 'POST' :
        cur_allergen.delete ()
        data ['form_is_valid'] = True
        allergens = Allergen.objects.all ()
        data ['html_list'] = render_to_string ('sneeze/allergen_list.partial.html', { 'allergens': allergens })
    else:
        context = { 'allergen': cur_allergen }
        data ['html_form'] = render_to_string ('sneeze/allergen_delete.partial.html', context, request = request)

    return JsonResponse (data)




# manage patients
#


def patient_list (request) :

    patients = Patient.objects.all ()

    return render (request, 'sneeze/patient_list.html', { 'patients': patients })



def save_patient_form (request, form, template_name) :

    data = dict ()

    if request.method == 'POST' :
        if form.is_valid ():
            form.save ()
            data ['form_is_valid'] = True
            patients = Patient.objects.all()
            data ['html_list'] = render_to_string ('sneeze/patient_list.partial.html', { 'patients': patients })
        else :
            data ['form_is_valid'] = False

    context = { 'form': form }
    data ['html_form'] = render_to_string (template_name, context, request = request)

    return JsonResponse (data)



def patient_create (request) :
    if request.method == 'POST' :
        form = PatientForm (request.POST)
    else :
        form = PatientForm ()

    return save_patient_form (request, form, 'sneeze/patient_create.partial.html')



def patient_update (request, pk) :
    try :
        cur_patient = Patient.objects.get (pk = pk)
    except Allergen.DoesNotExist :
        raise Http404 ("Patient does not exist")

    if request.method == 'POST' :
        form = PatientForm (request.POST, instance = cur_patient)
    else :
        form = PatientForm (instance = cur_patient)

    return save_patient_form (request, form, 'sneeze/patient_update.partial.html')



def patient_delete (request, pk) :
    try :
        cur_patient = Patient.objects.get (pk = pk)
    except Allergen.DoesNotExist :
        raise Http404 ("Patient does not exist")

    data = dict ()

    if request.method == 'POST' :
        cur_patient.delete ()
        data ['form_is_valid'] = True
        patients = Patient.objects.all ()
        data ['html_list'] = render_to_string ('sneeze/patient_list.partial.html', { 'patients': patients })
    else:
        context = { 'patient': cur_patient }
        data ['html_form'] = render_to_string ('sneeze/patient_delete.partial.html', context, request = request)

    return JsonResponse (data)




# manage reports
#


def report_list (request) :

    reports = Report.objects.all ()

    return render (request, 'sneeze/report_list.html', { 'reports': reports })



def save_report_form (request, form, template_name) :

    data = dict ()

    if request.method == 'POST' :
        if form.is_valid () :
            form.save ()
            data ['form_is_valid'] = True
            reports = Report.objects.all ()
            data ['html_list'] = render_to_string ('sneeze/report_list.partial.html', { 'reports': reports })
        else :
            data ['form_is_valid'] = False

    context = { 'form': form }
    data ['html_form'] = render_to_string (template_name, context, request = request)

    return JsonResponse (data)



def report_create (request) :
    if request.method == 'POST' :
        form = ReportForm (request.POST)
    else :
        form = ReportForm ()

    return save_report_form (request, form, 'sneeze/report_create.partial.html')



def report_detail (request, pk) :

    allergy_tests = AllergyTest.objects.filter (report = pk)

    return render (request, 'sneeze/report_detail.html', { 'allergy_tests': allergy_tests })



def report_delete (request, pk) :
    try :
        cur_report = Report.objects.get (pk = pk)
    except Report.DoesNotExist :
        raise Http404 ("Report does not exist")

    data = dict ()

    if request.method == 'POST' :
        cur_report.delete ()
        data ['form_is_valid'] = True
        reports = Report.objects.all ()
        data ['html_list'] = render_to_string ('sneeze/report_list.partial.html', { 'reports': reports })
    else :
        context = { 'report': cur_report }
        data ['html_form'] = render_to_string ('sneeze/report_delete.partial.html', context, request = request)

    return JsonResponse (data)

