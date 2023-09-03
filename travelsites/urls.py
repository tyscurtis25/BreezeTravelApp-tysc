from django.urls import path
from .views import showtripsPageView
from .views import showAfricaEgyptPageView
from .views import showAfricaTanzaniaPageView
from .views import showAsiaChinaPageView
from .views import showAsiaIndonesiaPageView
from .views import showAsiaJapanPageView
from .views import showAustraliaPageView
from .views import showCentralAmericaPageView
from .views import showEuropeFrancePageView
from .views import showEuropeItalyPageView
from .views import showMiddleEastPageView
from .views import showNorthAmericaArizonaPageView
from .views import showNorthAmericaHawaiiPageView
from .views import showSouthAmericaArgBrazilPageView
from .views import showSouthAmericaBrazilPageView
from .views import showSouthAmericaPeruPageView


urlpatterns = [
     path("", showtripsPageView, name="showtrips"),
     path("africa1/", showAfricaEgyptPageView, name="africa1"),
     path("africa2/", showAfricaTanzaniaPageView, name="africa2"),
     path("asia1/", showAsiaChinaPageView, name="asia1"),
     path("asia2/", showAsiaIndonesiaPageView, name="asia2"),
     path("asia3/", showAsiaJapanPageView, name="asia3"),
     path("australia/", showAustraliaPageView, name="australia"),
     path("centralamerica/", showCentralAmericaPageView, name="centralamerica"),
     path("europe1/", showEuropeFrancePageView, name="europe1"),
     path("europe2/", showEuropeItalyPageView, name="europe2"),
     path("middleeast/", showMiddleEastPageView, name="middleeast"),
     path("northamerica1/", showNorthAmericaArizonaPageView, name="northamerica1"),
     path("northamerica2/", showNorthAmericaHawaiiPageView, name="northamerica2"),
     path("southamerica1/", showSouthAmericaArgBrazilPageView, name="southamerica1"),
     path("southamerica2/", showSouthAmericaBrazilPageView, name="southamerica2"),
     path("southamerica3/", showSouthAmericaPeruPageView, name="southamerica3"),
]
