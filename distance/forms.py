# imports
import json

from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model

from distance import models as distance_models


User = get_user_model()

# End: imports -----------------------------------------------------------------

class WorkoutForm(forms.ModelForm):
    required_css_class = 'required font-bold'

    class Meta:
        model = distance_models.Workout
        exclude = ['user', 'created']
        #fields = []


    def __init__(self, *args, **kwargs):
        super(type(self), self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-2'})

        self.fields['date'].widget.attrs.update({'class': 'flatpickr form-control'})
        self.fields['comment'].widget.attrs.update({'rows': 5})
        self.fields['distance'].widget.attrs.update({'placeholder': 'Eks: 8,2 km'})


#
# class ExampleModelForm(forms.ModelForm):
#     # duration = forms.TimeField(input_formats=MIN_FORMATS, required=False)
#     required_css_class = 'required font-bold'
#
#     class Meta:
#         model = User
#         exclude = ['nr']
#         widgets = {
#             'song': select2_forms.Select2Widget(),
#             'song2': select2_forms.Select2Widget(),
#         }
#
#     def __init__(self, *args, **kwargs):
#         super(type(self), self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs.update({'class': 'form-control'})
#
#         self.fields['duration'].widget.attrs.update({'placeholder': 'min'})
#         # self.fields['duration'].widget.format = "%M"
#
#         self.fields['start'].widget.attrs.update({'placeholder': 'hh:mm', 'readonly': '1'})
#         self.fields['start'].widget.format = "%H:%M"
#
#         self.fields['description'].widget.attrs.update({'class': 'tinymce'})
#
#
# class ExampleForm(forms.Form):
#     search = forms.CharField(required=False, label="Søk")
#     tag = forms.ChoiceField(required=False, widget=select2_forms.Select2Widget())
#     # tag = forms.ChoiceField(required=False)
#     lead = forms.ChoiceField(required=False, widget=select2_forms.Select2Widget(), label="Instruktør (lead)")
#     # lead = forms.ChoiceField(required=False, label="Instruktør (lead)")
#     follow = forms.ChoiceField(required=False, widget=select2_forms.Select2Widget(), label="Instruktør (follow)")
#     bulk = forms.IntegerField(required=False, label="Bolk")
#     day = forms.IntegerField(required=False, label="Dag")
#     semester_char = forms.CharField(required=False, label="Semester")
#     external = forms.BooleanField(initial=False, required=False, label="Eksternkurs")
#
#     def __init__(self, *args, **kwargs):
#         super(type(self), self).__init__(*args, **kwargs)
#         for field in self.fields:
#             # pass
#             self.fields[field].widget.attrs.update({'class': 'course-filter form-control'})
#
#         self.fields['external'].widget.attrs.update({'class': 'invisible'})
#
#         self.fields['search'].widget.attrs.update({'placeholder': 'Søk på tittel...', 'autofocus': True})
#         self.fields['semester_char'].widget.attrs.update({'placeholder': 'Eks: H2019, V2020',})
#
#         # self.fields['tag'].choices = [(-1, '-----')]
#         self.fields['tag'].choices += [(tag.id, tag.title) for tag in song_models.Tag.getQueryset(["course"])]
#         self.fields['tag'].widget.attrs.update({'class': 'form-control course-filter'})
#
#         # self.fields['lead'].choices = [(-1, '-----')]
#         self.fields['lead'].choices += [(lead.id, lead) for lead in User.objects.all()]
#
#         # self.fields['follow'].choices = [(-1, '-----')]
#         self.fields['follow'].choices += [(follow.id, follow) for follow in User.objects.all()]
