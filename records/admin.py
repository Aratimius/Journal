from django.contrib import admin

from records.models import Entry, Objective


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
    )


@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
    )
