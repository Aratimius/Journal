from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit
from django.forms import ModelForm
from records.models import Entry, Objective


class EntryCreateForm(ModelForm):
    """Форма для создания"""

    class Meta:
        model = Entry
        exclude = ("status",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_read_only = True
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            Div(
                Div("is_purpose", css_class="md:w-[10%]"),
                Div("is_private", css_class="md:w-[80%]"),
                css_class="md:flex md:justify-between",
            ),
            "title",
            "description",
            "start_time",
            "end_time",
            Submit(
                "submit",
                "Сохранить",
                css_class="text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2",
            ),
        )


class EntryUpdateForm(ModelForm):
    """Форма для редактирования"""

    class Meta:
        model = Entry
        exclude = (
            "status",
            "is_purpose",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            Div(
                Div("is_private", css_class="md:w-[80%]"),
                css_class="md:flex md:justify-between",
            ),
            "title",
            "description",
            "start_time",
            "end_time",
            Submit(
                "submit",
                "Сохранить",
                css_class="text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2",
            ),
        )


class ObjectiveForm(ModelForm):
    """Модель задачи"""

    class Meta:
        model = Objective
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            Div(
                Div("title", css_class="md:w-[40%]"),
                Div("is_complete", css_class="md:w-[90%]"),
                css_class="md:flex md:justify-between",
            ),
            "description",
            "time",
        )


class ObjectiveCreateForm(ModelForm):
    """Модель создания и изменения задачи"""

    class Meta:
        model = Objective
        fields = "__all__"

    # def clean(self):
    #     cleaned_data = super().clean()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = "border p-8"
        self.helper.layout = Layout(
            Div(
                Div("title", css_class="md:w-[40%]"),
                Div("is_complete", css_class="md:w-[90%]"),
                css_class="md:flex md:justify-between",
            ),
            "description",
            "time",
            Submit(
                "submit",
                "Сохранить",
                css_class="text-white bg-gradient-to-br from-green-400 to-blue-600 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-green-200 dark:focus:ring-green-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2",
            ),
        )
