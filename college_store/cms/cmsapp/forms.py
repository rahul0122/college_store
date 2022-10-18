from django import forms

from .models import Person, Course

DEMO_CHOICES = (
    ("1", "debit Note Book"),
    ("2", "Pen"),
    ("3", "Exam Paper"),

)


class PersonCreationForm(forms.ModelForm):
    materials = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple(), choices=DEMO_CHOICES)

    class Meta:
        model = Person
        fields = '__all__'

        widgets = {
            'date_of_birth': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_id': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'purpose': forms.Select(attrs={'class': 'form-control'}),
            'materials': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')
