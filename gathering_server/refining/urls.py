from django.urls import path

from gathering_server.refining.views import RefiningCalculatorView

specpatterns = []

refiningpatterns = [
    path('refining/calculate', RefiningCalculatorView.as_view(), name="refinig_calculator")
]

urlpatterns = specpatterns + refiningpatterns
