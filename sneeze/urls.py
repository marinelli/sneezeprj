
from django.conf.urls     import url
from django.views.generic import TemplateView

from .                    import views



urlpatterns = [
    url ( r'^$' , TemplateView.as_view (template_name = 'home.html') , name = 'home' ),
]


urlpatterns.extend ([
    url ( r'^allergen/$'                         , views.allergen_list       , name = 'allergen_list'       ),
    url ( r'^allergen/create/$'                  , views.allergen_create     , name = 'allergen_create'     ),
    url ( r'^allergen/(?P<pk>\w+)/update/$'      , views.allergen_update     , name = 'allergen_update'     ),
    url ( r'^allergen/(?P<pk>\w+)/delete/$'      , views.allergen_delete     , name = 'allergen_delete'     ),
])


urlpatterns.extend ([
    url ( r'^patient/$'                          , views.patient_list        , name = 'patient_list'        ),
    url ( r'^patient/create/$'                   , views.patient_create      , name = 'patient_create'      ),
    url ( r'^patient/(?P<pk>\w+)/update/$'       , views.patient_update      , name = 'patient_update'      ),
    url ( r'^patient/(?P<pk>\w+)/delete/$'       , views.patient_delete      , name = 'patient_delete'      ),
])


urlpatterns.extend ([
    url ( r'^report/$'                           , views.report_list         , name = 'report_list'         ),
    url ( r'^report/create/$'                    , views.report_create       , name = 'report_create'       ),
    url ( r'^report/(?P<pk>\d+)/delete/$'        , views.report_delete       , name = 'report_delete'       ),
])


urlpatterns.extend ([
    url ( r'^report/(?P<report_id>\d+)/$'        , views.allergy_test_list   , name = 'allergy_test_list'   ),
    url ( r'^report/(?P<report_id>\d+)/create/$' , views.allergy_test_create , name = 'allergy_test_create' ),
    url ( r'^report/\d+/(?P<pk>\d+)/update/$'    , views.allergy_test_update , name = 'allergy_test_update' ),
    url ( r'^report/\d+/(?P<pk>\d+)/delete/$'    , views.allergy_test_delete , name = 'allergy_test_delete' ),
])

