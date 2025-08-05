from django import forms
from .models import Flat

# Data for Indian States and Major Cities
# In a real-world application, you might want to store this in your database
INDIAN_STATES_CITIES = {
    'Andaman & Nicobar Islands': ['Port Blair', 'Garacharma', 'Bambooflat'],
    'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore', 'Kurnool', 'Rajahmundry', 'Tirupati'],
    'Arunachal Pradesh': ['Itanagar', 'Naharlagun'],
    'Assam': ['Guwahati', 'Silchar', 'Dibrugarh', 'Jorhat', 'Nagaon', 'Tinsukia'],
    'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur', 'Purnia', 'Darbhanga'],
    'Chandigarh': ['Chandigarh'],
    'Chhattisgarh': ['Raipur', 'Bhilai', 'Korba', 'Bilaspur', 'Durg'],
    'Dadra & Nagar Haveli and Daman & Diu': ['Daman', 'Diu', 'Silvassa'],
    'Delhi': ['Delhi', 'New Delhi'],
    'Goa': ['Panaji', 'Margao', 'Vasco da Gama'],
    'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot', 'Bhavnagar', 'Jamnagar'],
    'Haryana': ['Faridabad', 'Gurgaon', 'Panipat', 'Ambala', 'Yamunanagar', 'Rohtak'],
    'Himachal Pradesh': ['Shimla', 'Solan', 'Dharamshala'],
    'Jammu & Kashmir': ['Srinagar', 'Jammu', 'Anantnag'],
    'Jharkhand': ['Dhanbad', 'Ranchi', 'Jamshedpur', 'Bokaro Steel City', 'Deoghar'],
    'Karnataka': ['Bangalore', 'Hubli-Dharwad', 'Mysore', 'Gulbarga', 'Mangalore', 'Belgaum'],
    'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Kollam', 'Thrissur'],
    'Ladakh': ['Leh', 'Kargil'],
    'Lakshadweep': ['Kavaratti'],
    'Madhya Pradesh': ['Indore', 'Bhopal', 'Jabalpur', 'Gwalior', 'Ujjain', 'Sagar'],
    'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Thane', 'Nashik', 'Aurangabad'],
    'Manipur': ['Imphal'],
    'Meghalaya': ['Shillong'],
    'Mizoram': ['Aizawl'],
    'Nagaland': ['Dimapur', 'Kohima'],
    'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Puri', 'Sambalpur'],
    'Puducherry': ['Puducherry', 'Karaikal'],
    'Punjab': ['Ludhiana', 'Amritsar', 'Jalandhar', 'Patiala', 'Bathinda'],
    'Rajasthan': ['Jaipur', 'Jodhpur', 'Kota', 'Bikaner', 'Ajmer', 'Udaipur'],
    'Sikkim': ['Gangtok'],
    'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli', 'Salem', 'Tirunelveli'],
    'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Karimnagar', 'Ramagundam'],
    'Tripura': ['Agartala'],
    'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Ghaziabad', 'Agra', 'Meerut', 'Varanasi'],
    'Uttarakhand': ['Dehradun', 'Haridwar', 'Roorkee'],
    'West Bengal': ['Kolkata', 'Asansol', 'Siliguri', 'Durgapur', 'Bardhaman'],
}

class FlatFrom(forms.ModelForm):
    # Create a list of tuples for the state choices
    state_choices = [('Select','Select')] + [(state , state) for state  in INDIAN_STATES_CITIES.keys()]
    # Override the state and city fields to use our dynamic choices
    state =  forms.ChoiceField(choices=state_choices,required=True,widget=forms.Select(attrs={'class' : 'form-control'}))
    city  = forms.ChoiceField(choices=[('Select','Select')] , required=True , widget=forms.Select(attrs={'class' : 'form-control'}))
    class Meta:
        model = Flat
        exclude = ('listed_by', 'is_available')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'bhk': forms.Select(attrs={'class': 'form-control'}),
            'bathrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'furnishing': forms.Select(attrs={'class': 'form-control'}),
            'area_sqft': forms.NumberInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'}),
            'deposit': forms.NumberInput(attrs={'class': 'form-control'}),
            'available_from': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            # Use CheckboxInput for boolean fields for a better UI
            'parking': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'lift': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'security': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'power_backup': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gym': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'swimming_pool': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'wifi': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'pets_allowed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # If a state is already selected (e.g., in a form submission),
        # populate the city choices for that state.
        if 'state' in self.data:
            try:
                state_name = self.data.get('state')
                self.fields['city'].choices = [(city, city) for city in INDIAN_STATES_CITIES[state_name]]
            except (ValueError, KeyError, TypeError):
                self.fields['city'].choices = [('Select', 'Select')]
        elif self.instance.pk:
            # If the form is bound to a model instance, populate cities based on the instance's state
            try:
                self.fields['city'].choices = [(city, city) for city in INDIAN_STATES_CITIES[self.instance.state]]
            except (KeyError, TypeError):
                self.fields['city'].choices = [('Select', 'Select')]

class FlatEditForm(forms.ModelForm):
    class Meta: 
        model = Flat
        exclude = ['listed_by', 'listed_on', 'updated_on']
        

BHK_CHOICES = [
    ('', 'Any BHK'),
    (1, '1 BHK'),
    (2, '2 BHK'),
    (3, '3 BHK'),
    (4, '4 BHK'),
    (5, '5+ BHK'),
]

class FlatFilterForm(forms.Form):
    state = forms.ChoiceField(
        choices=[('', 'Any State')] + [(state, state) for state in INDIAN_STATES_CITIES.keys()],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    city = forms.ChoiceField(
        choices=[('', 'Any City')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    bhk = forms.ChoiceField(
        choices=BHK_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'state' in self.data:
            state = self.data.get('state')
            if state in INDIAN_STATES_CITIES:
                self.fields['city'].choices = [('', 'Any City')] + [
                    (city, city) for city in INDIAN_STATES_CITIES[state]
                ]
