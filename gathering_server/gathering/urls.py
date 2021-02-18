# Django imports
from django.urls import path

# Views imports
from gathering_server.gathering.views import (
    GatheringCreateView,
    GatheringListView,
    GatheringByIdView,
    GatheringDeleteView,
    GatheringUpdateView
)

from gathering_server.gathering.views import (
    SpecCreateView,
    SpecReadView,
    SpecUpdateView
)

specpatterns = [
    path('spec/new', SpecCreateView.as_view(), name="new_spec_collection"),
    path('spec', SpecReadView.as_view(), name="read_spec"),
    path('spec/update', SpecUpdateView.as_view(), name="update_spec")
]

gatheringpatterns = [
    path('gather/new', GatheringCreateView.as_view(), name="new_gather_collection"),
    path('gather/list', GatheringListView.as_view(), name="list_gather_collections"),
    path('gather/list-id', GatheringByIdView.as_view(), name='list_gather_by-id_collection'),
    path('gather/delete', GatheringDeleteView.as_view(), name='delete_gather_collection'),
    path('gather/update', GatheringUpdateView.as_view(), name='update_gather_collection')
]

urlpatterns = specpatterns + gatheringpatterns
