from django.urls import path
from records.apps import RecordsConfig
from records.views import (
    EntryListView,
    PrivateEntryListView,
    PastEntryListView,
    PresentEntryListView,
    FutureEntryListView,
    EntryCreateView,
    EntryUpdateView,
    EntryDetailView,
    EntryDeleteView,
    ObjectiveUpdateView,
    ObjectiveDeleteView,
    ObjectiveCreateView,
)

app_name = RecordsConfig.name

urlpatterns = [
    # ЗАПИСИ
    path("list/", EntryListView.as_view(), name="list"),
    path("private_list/", PrivateEntryListView.as_view(), name="private_list"),
    path("past_list/", PastEntryListView.as_view(), name="past_list"),
    path("present_list/", PresentEntryListView.as_view(), name="present_list"),
    path("future_list/", FutureEntryListView.as_view(), name="future_list"),
    path("create/", EntryCreateView.as_view(), name="create"),
    path("update/<int:pk>/", EntryUpdateView.as_view(), name="update"),
    path("detail/<int:pk>/", EntryDetailView.as_view(), name="detail"),
    path("delete/<int:pk>/", EntryDeleteView.as_view(), name="delete"),
    # ЗАДАЧИ
    path("create_obj/", ObjectiveCreateView.as_view(), name="create_obj"),
    path("update_obj/<int:pk>/", ObjectiveUpdateView.as_view(), name="update_obj"),
    path("delete_obj/<int:pk>/", ObjectiveDeleteView.as_view(), name="delete_obj"),
]
