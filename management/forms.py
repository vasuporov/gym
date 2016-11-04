from django import forms
from models import FeesStructure

PHONE_FIELD_REGEX = r'^\+?1?[\d\- ]{8,23}$'


class AddGymMemberForm(forms.Form):
    first_name = forms.CharField(max_length=256, label='First Name', widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=256, label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    gender = forms.ChoiceField(label='Gender', widget=forms.Select, choices=(("male", "male"), ("female", "female")))
    date_of_birth = forms.DateField(label='Date of birth', widget=forms.TextInput(attrs={'class':'datepicker'}))
    phone = forms.RegexField(regex=PHONE_FIELD_REGEX, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    photo = forms.ImageField(required=False)
    height = forms.DecimalField(label="Height", required=False)
    weight = forms.IntegerField(label="Weight", required=False)
    biceps_right = forms.IntegerField(label="Biceps Right", required=False)
    biceps_left = forms.IntegerField(label="Biceps Left", required=False)
    triceps_right = forms.IntegerField(label="Triceps Right", required=False)
    triceps_left = forms.IntegerField(label="Triceps Left", required=False)
    joining_date = forms.DateField(label='Joining Date', widget=forms.TextInput(attrs={'class':'datepicker'}))

    def __init__(self, gym, *args, **kwargs):
        super(AddGymMemberForm, self).__init__(*args, **kwargs)
        fees_structures = FeesStructure.objects.filter(gym=gym).all()
        if fees_structures:
            self.fields['fees_structure'] = forms.ChoiceField(label='Fees Structure', choices=[(fees_structure.id,
                                                              str(fees_structure.fees_structure_type) + " - Rs. " +
                                                              str(fees_structure.fees_amount))
                                                              for fees_structure in fees_structures])
        else:
            self.fields['fees_structure'] = forms.ChoiceField(label='Fees Structure', choices=[("None", "None")])
