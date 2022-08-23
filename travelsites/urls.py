from django.urls import path
from .views import showtripsPageView
from .views import showAfricaPageView
from .views import showAsiaPageView
from .views import showAustraliaPageView
from .views import showEuropePageView
from .views import showNorthAmericaPageView
from .views import showSouthAmericaPageView

urlpatterns = [
     path("", showtripsPageView, name="showtrips"),
     path("africa/", showAfricaPageView, name="africa"),
     path("asia/", showAsiaPageView, name="asia"),
     path("australia/", showAustraliaPageView, name="australia"),
     path("europe/", showEuropePageView, name="europe"),
     path("northamerica/", showNorthAmericaPageView, name="northamerica"),
     path("southamerica/", showSouthAmericaPageView, name="southamerica"),
]
