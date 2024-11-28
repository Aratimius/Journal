from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.db.models import Q
from records.forms import (
    EntryCreateForm,
    EntryUpdateForm,
    ObjectiveForm,
    ObjectiveCreateForm,
)
from records.models import Entry, Objective
from django.http import Http404


#  ЗАПИСИ
class PrivateEntryListView(LoginRequiredMixin, ListView):
    """Вывод списка личных записей"""

    model = Entry
    template_name = "records/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(Q(is_private=True) & Q(user=user))

        return queryset


class PastEntryListView(LoginRequiredMixin, ListView):
    """Вывод списка достигнутых целей"""

    model = Entry
    template_name = "records/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(is_purpose=True, status="PAST", user=user)

        return queryset


class PresentEntryListView(LoginRequiredMixin, ListView):
    """Вывод списка целей, который находятся в процессе достижения"""

    model = Entry
    template_name = "records/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(is_purpose=True, status="PRESENT", user=user)

        return queryset


class FutureEntryListView(LoginRequiredMixin, ListView):
    """Вывод списка целей, которые предстоит достичь"""

    model = Entry
    template_name = "records/list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(is_purpose=True, status="FUTURE", user=user)

        return queryset


class EntryListView(LoginRequiredMixin, ListView):
    """Просмотре всех записей пользователя"""

    model = Entry

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        queryset = queryset.filter(user=user)
        # ПОИСК ПО ЗАГОЛОВКУ ИЛИ ОПИСАНИЮ:
        search = self.request.GET.get("search", "")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | Q(description__icontains=search)
            )
            return queryset
        else:
            return queryset


class EntryCreateView(LoginRequiredMixin, CreateView):
    """Создание записи"""

    model = Entry
    success_url = reverse_lazy("records:list")
    form_class = EntryCreateForm

    def form_valid(self, form):
        """Присвоение статуса записи, если запись является целью,
        по дате начала и конца"""

        entry = form.save()
        user = self.request.user
        entry.user = user

        now = datetime.now()
        if entry.is_purpose:
            if entry.end_time:
                if entry.end_time.date() < now.date():
                    entry.status = "PAST"
                elif entry.start_time.date() <= now.date():
                    entry.status = "PRESENT"
                else:
                    entry.status = "FUTURE"
            elif entry.start_time.date() <= now.date():
                entry.status = "PRESENT"
            else:
                entry.status = "FUTURE"
        entry.save()
        return super().form_valid(form)

    def get_success_url(self):
        entry_pk = self.object.pk
        return reverse_lazy("records:update", kwargs={"pk": entry_pk})


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование записи"""

    model = Entry
    form_class = EntryUpdateForm

    def get_object(self, queryset=None):
        """Как только зашли на страницу редактирования записи,
        она получает статус последней просмотренной страницы"""

        object = super().get_object()
        for entry in Entry.objects.all():
            entry.last_viewed = False
            entry.save()
        entry = Entry.objects.get(pk=object.pk)
        entry.last_viewed = True
        entry.save()
        return object

    def form_valid(self, form):
        """Обновление статуса записи, если запись является целью,
        по дате начала и конца"""

        entry = form.save()
        user = self.request.user
        entry.user = user

        now = datetime.now()
        if entry.is_purpose:
            if entry.end_time:
                if entry.end_time.date() < now.date():
                    entry.status = "PAST"
                elif entry.start_time.date() <= now.date():
                    entry.status = "PRESENT"
                else:
                    entry.status = "FUTURE"
            elif entry.start_time.date() <= now.date():
                entry.status = "PRESENT"
            else:
                entry.status = "FUTURE"

        #  ДОБАВИТЬ ФОРМСЕТ:
        formset = self.get_context_data()["formset"]
        if formset.is_valid():
            formset.instance = entry
            formset.save()

        entry.save()
        return super().form_valid(form)

    def get_success_url(self):
        entry_pk = self.kwargs["pk"]
        return reverse_lazy("records:update", kwargs={"pk": entry_pk})

    def get_context_data(self, **kwargs):
        """Определяем формсет"""
        context_data = super().get_context_data(**kwargs)
        ObjectiveFormset = inlineformset_factory(
            Entry, Objective, form=ObjectiveForm, extra=0
        )
        if self.request.method == "POST":
            context_data["formset"] = ObjectiveFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = ObjectiveFormset(instance=self.object)

        return context_data


class EntryDetailView(LoginRequiredMixin, DetailView):
    """Просмотр записи"""

    model = Entry

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        entry = Entry.objects.get(pk=self.object.pk)
        objectives = Objective.objects.filter(entry=entry)
        context_data["objectives"] = objectives
        return context_data


class EntryDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление записи"""

    model = Entry
    success_url = reverse_lazy("records:list")


#  ЗАДАЧИ:
class ObjectiveCreateView(LoginRequiredMixin, CreateView):
    """Создание задачи"""

    model = Objective
    form_class = ObjectiveCreateForm

    def get_success_url(self):
        """Редиректит на страницу редактирования записи"""
        return reverse_lazy("records:update", kwargs={"pk": self.entry.pk})

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data()
        entry = Entry.objects.get(last_viewed=True)
        context_data["entry_pk"] = entry.pk
        return context_data

    def form_valid(self, form):
        """Проверка валидности задачи"""
        objective = form.save()
        self.entry = Entry.objects.get(last_viewed=True)
        if self.entry.status == "PAST" and objective.is_complete is not True:
            raise Http404("Задачи к достигнутым целям должны считаться выполненными")
        objective.entry = self.entry
        objective.save()
        return super().form_valid(form)


class ObjectiveDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление задачи"""

    model = Objective
    template_name = "records/entry_confirm_delete.html"

    def get_success_url(self):
        objective_pk = self.kwargs["pk"]
        objective = Objective.objects.get(pk=objective_pk)
        return reverse_lazy("records:update", kwargs={"pk": objective.entry.pk})


class ObjectiveUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирование задачи"""

    model = Objective
    form_class = ObjectiveCreateForm

    def get_success_url(self):
        """Редирект на страницу редактирования цели"""
        return reverse_lazy("records:update", kwargs={"pk": self.entry.pk})

    def form_valid(self, form):
        """Проверка валидности задачи"""
        objective = self.object
        self.entry = Entry.objects.get(last_viewed=True)
        if self.entry.status == "PAST" and not objective.is_complete:
            raise Http404("Задачи к достигнутым целям должны считаться выполненными")
        objective.entry = self.entry
        objective.save()
        return super().form_valid(form)
