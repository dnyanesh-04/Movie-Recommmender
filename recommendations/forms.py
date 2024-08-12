from django import forms
from .models import Movie

class MovieAdminForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MovieAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['recommendations'].queryset = Movie.objects.exclude(pk=self.instance.pk)
