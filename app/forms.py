from django.core.urlresolvers import reverse 
from django import forms 
from django.core.validators import RegexValidator
from models import State, City 

#crispy 
from crispy_forms.helper import FormHelper  
from crispy_forms.layout import Submit, HTML, Layout, Div , Field
from crispy_forms.bootstrap import FormActions 


class StateCreate(forms.ModelForm):
	class Meta:
		model = State 
		fields = '__all__'

#     def __init__(self, *args, **kwargs):
#     super(StateCreate, self).__init__(*args, **kwargs)
#     self.helper = FormHelper()
#     self.helper.form_method = 'get'
#     self.helper.form_action = 'state_create'
#     # customize the crispy forms
#     self.helper.layout = Layout()


# must = 12 
class EditCity(forms.ModelForm):
	class Meta:
		model = City 
		fields = '__all__'
	
	def __init__(self, *args, **kwargs):
		super(EditCity, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('edit_city', kwargs= {'pk': self.instance.pk})
		    # customize the crispy forms
		self.helper.layout = Layout(
		    								Div('state','name','county', css_class='col-sm-6'),
		    								Div('latitude','longitude','zipcode', css_class='col-sm-6'),
		    								Div( FormActions(Submit('submit','Save')),css_class='col-sm-2 col-md-2',style='margin-top:25px;')
		    						)

# class EditCity(forms.ModelForm):
#     class Meta:
#         model = City
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super(EditCity, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.form_action = reverse('edit_city', kwargs={'pk': self.instance.pk })
#         # self.helper.add_input(Submit('submit', 'Search'))
#         self.helper.layout = Layout(
#                     Div('state', 'name', 'county', css_class='col-sm-6'),
#                     Div('latitude', 'longitude', 'zipcode', css_class='col-sm-6'),
#                     Div(FormActions(Submit('submit', 'Save')), css_class='col-sm-12')
#             )



class CityCreate(forms.ModelForm):
	class Meta:
		model = City 
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(CityCreate, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_action = reverse('edit_city', kwargs= {'pk': self.instance.pk})
		    # customize the crispy forms
		self.helper.layout = Layout(
		    								Div('state','name','county', css_class='col-sm-6'),
		    								Div('latitude','longitude','zipcode', css_class='col-sm-6'),
		    								Div( FormActions(Submit('submit','Save')), css_class='col-md-12')
		    						)

# 	def __init__(self, *args, **kwargs):
#     super(CityCreate, self).__init__(*args, **kwargs)
#     self.helper = FormHelper()
#     self.helper.form_method = 'get'
#     self.helper.form_action = 'city_create'
#     # customize the crispy forms
#     self.helper.layout = Layout()





#to accept only valid chars ( no numbers )
class CitySearchForm(forms.Form):  
	# * to take all the chars 
    letters_only = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed!')
    city = forms.CharField(required=True, initial="Orem", validators=[letters_only])
    state = forms.CharField(required=True, initial="Utah", validators=[letters_only])
    # STATES = State.objects.all().values_list('id','name')
    # state_select = forms.ChoiceField(choice=STATES)


    def __init__(self, *args, **kwargs):
        super(CitySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_action = 'city_search'
        # customize the crispy forms
        self.helper.layout = Layout(
        							# Div ('city', 'state', FormActions(Submit('submit','Search',css_class="btn-primary")))
        							Div('city', css_class='col-sm-5 col-md-5', style='max_width=220px;'),
        							Div('state', css_class='col-sm-5 col-md-5'),
        							Div( FormActions(Submit('submit','Search')),css_class='col-sm-2 col-md-2',style='margin-top:25px;')
        						)

class EditState(forms.ModelForm):

    class Meta:
        model = State
        fields = '__all__'

class CreateState(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'



    def __init__(self, *args, **kwargs):
        super(EditState, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_state', kwargs={'pk': self.instance.pk})
        self.helper.layout = Layout(
                    Div(
                        Div('name', css_class='col-md-10'),
                        Div('abbreviation', css_class='col-md-2'),
                        css_class='row'
                    ),
                    Div(
                        Div(FormActions(Submit('submit', 'Submit')), css_class="col-md-12"),
                        css_class='row'
                    )
            )


        # self.helper.add_input(Submit('submit', 'Submit'))


    # STATES1 = (
    # 			('1','Texas'),
    # 			('2', 'Utah'),
    # 			('3', 'California')
    # 		  )

    # STATES2 = State.objects.all().values_list('id','name')

    # state_select = forma.ChoiceField(choices=STATES2)


