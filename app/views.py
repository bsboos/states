
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from app.models import State, City, StateCapital

from django.utils.html import escape

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from app.forms import CitySearchForm, CityCreate, EditCity, EditState, CreateState

# Create your views here.
@login_required
def edit_state(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    form = EditState(request.POST or None, instance=state)

    context['form'] = form

    if form.is_valid():
        form.save()

        return redirect('/state_list/')

    return render(request, 'state_edit.html', context)


@login_required
def create_state(request):

    context = {}

    form = StateCreate(request.GET)

    context['form'] = form

    if form.is_valid():
        form.save()

    return render(request, 'create_state.html', context)

@login_required
def delete_city(request, pk):

    City.objects.get(pk=pk).delete()

    return redirect('/city_list/')

@login_required
def edit_city(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city

    if request.method == 'POST':

        form = EditCity(request.POST or None, instance=city)

        context['form'] = form

        if form.is_valid():
            form.save()

            return redirect('/city_list/')

    return render(request, 'city_edit.html', context)


@login_required
def create_city(request):

    context = {}

    form = CityCreate(request.GET)

    context['form'] = form

    if form.is_valid():
        form.save()

    return render(request, 'create_city.html', context)



def city_search_post(request):

    context = {}

    context['states'] = State.objects.all()

    form = CitySearchForm(request.POST)

    context['form'] = form

    if request.method == 'POST':

        if form.is_valid():
            city = form.cleaned_data.get('city', 'Orem')
            state = form.cleaned_data.get('state', 'Utah')

            context['cities'] = City.objects.filter(name=city, state__name=state)

    return render(request, 'city_search_post.html', context)

def city_search(request):

    context = {}

    form = CitySearchForm(request.GET)

    context['form'] = form

    if form.is_valid():

        city = form.cleaned_data.get("city", "Orem")
        state = form.cleaned_data.get("state", "Utah")

        cities = City.objects.filter(name=city, state__name=state)    
        context['cities'] = cities

    return render(request, 'city_search.html', context)









































# from django.shortcuts import render

# from django.http import HttpResponse

# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from app.models import State
# from app.models import StateCapital
# from app.models import City
# from django.utils.html import escape
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from django.views.generic.list import ListView 
# from django.views.generic.detail import DetailView 
# from app.forms import CitySearchForm, CityCreate, EditCity, StateCreate

# # from django.views.generic.edit import FormView
# from django.shortcuts import render_to_response




# # Create your views here.

# # form view
# # the idea here is we don't want to get pure HTML file  



# @login_required
# def delete_state(request, pk):
#     context = {}
#     state = State.objects.get(pk=pk).delete()
#     return redirect('/state_list/')
# def create_state(request):
#     context = {}
#     form = StateCreate(request.GET)
#     context['form'] = form
#     if form.is_valid():
#         form.save()
#     return render(request, 'create_city.html', context)


# def edit_state(request, pk):
#     context = {}
#     state = State.objects.get(pk=pk)
#     context['state'] = state
#     form = EditCity(request.POST or None, instance=state)
#     context['form'] = form
#     if form.is_valid():
    
#         form.save()
#         return redirect('/state_list/')
#     return render(request, 'state_edit.html', context)


# @login_required
# def delete_city(request, pk):
#     context = {}
#     city = City.objects.get(pk=pk).delete()
#     return redirect('/city_list/')

    
# def edit_city(request, pk):
#     context = {}
#     city = City.objects.get(pk=pk)
#     context['city'] = city
#     form = EditCity(request.POST or None, instance=city)
#     context['form'] = form
#     if form.is_valid():
    
#         form.save()
#         return redirect('/city_list/')
#     return render(request, 'city_edit.html', context)



# def create_city(request):
#     context = {}
#     form = CityCreate(request.GET)
#     context['form'] = form
#     if form.is_valid():
#         form.save()
#     return render(request, 'create_city.html', context)



# def city_search(request):
#     context = {}
#     form = CitySearchForm(request.GET)
#     context['form'] = form
#     if form.is_valid():
#         city = form.cleaned_data.get("city", "Orem")
#         state = form.cleaned_data.get("state", "Utah")
        
#         cities = City.objects.filter(name=city, state__name=state)
#         context['cities'] = cities
#     return render (request, 'city_search.html', context)




def city_search_post(request):
	context={}
	form = CitySearchForm(request.POST)

	context['form'] = form 

	if request.method == 'POST': #check the method type
		if form.is_valid():
			city = form.cleaned_data.get('city','Orem')
			state = form.cleaned_data.get('state', 'Utah')

			context['cities'] = City.objects.filter(name=city, state__name=state)


	return render(request,'city_search_post.html', context)




# def city_search(request):
# 	context = {}
# 	form = CitySearchForm1(request.GET) #passing the data
#     context['form'] = form
	
# 	if form.is_valid():
# 		city = form.cleaned_data.get("city","Orem")
# 		state = form.cleaned_data.get("state","Utah")
# 		cities = City.objects.filter(name=city, state__name=state)
# 		context['cities'] = cities 
	
# 	return render(request,'city_search.html',context)


    # if request.method == 'POST':
    #     form = CitySearchForm(request.POST)
    #     context["form"] = form

    #     if form.is_valid(): #clean the database input " sanatize the db "
    #         name = "%s" % form.cleaned_data['name']
    #         state = form.cleaned_data['state']


    #         context['city_list'] = City.objects.filter(name__startswith=name, state__name__startswith=state)

    #         context['valid'] = "is valid"
    #         return render_to_response( "city_search.html", context, context_instance=request_context )

    #     else:
    #         context['valid'] = form.errors



    #         return render_to_response( "city_search.html", context, context_instance=request_context )

    # else:
    #     form = CitySearchForm()
    #     context["form"] = form

    #     return render_to_response( "city_search.html", context, context_instance=request_context )






# class view 
class StatecapitalDetailView(DetailView):
	model = StateCapital 
	template_name = "statecapital_detail.html"
	context_object_name = "statecapital"

class StatecapitalListView(ListView):  
    model = StateCapital
    template_name = "statecapital_list.html"
    # over riding where it's importing the calss 

    context_object_name = "statecapitals"


class CityDetailView(DetailView):
	model = City 
	template_name = "city_detail.html"
	context_object_name = "city"

class CityListView(ListView):  
    model = City
    template_name = "city_list.html"
    # over riding where it's importing the calss 

    context_object_name = "cities"



class StateDetailView(DetailView):
	model = State 
	template_name = "state_detail.html"
	context_object_name = "state"

class StateListView(ListView):  
    model = State
    template_name = "state_list.html"
    # over riding where it's importing the calss 

    context_object_name = "states"





# MA CAPOITALAAA
def statecapital_detail(request , pk ):
	context = {}

	statecapital = StateCapital.objects.get(pk = pk)

	context['statecapital'] = statecapital 

	return render(request, 'statecapital_detail.html', context)

def statecapital_list(request):
	context = {} 

	statecapitals = StateCapital.objects.all()

	context['statecapitals'] =  statecapitals

	return render(request, 'statecapital_list.html' , context )



# MA CITIZIA 
def city_detail(request , pk ):
	context = {}

	city = City.objects.get(pk = pk)

	context['city'] = city 

	return render(request, 'city_detail.html', context)

def city_list(request):
	context = {} 
	#we are setting the defult value of state pk incase the URL returned a non exisited pk
	state_pk = request.GET.get('state',140)

	cities = City.objects.filter(state__pk =  state_pk)

	# the dict have two keys 
	# state = [ the vaues are all the states ]
	# cities =  [ with all the cities ]
	context['cities'] = cities 
	context['state'] = State.objects.all()

	return render(request, 'city_list.html' , context )





# MA STATA
def state_detail( request, pk ):
	context= {} 

	state = State.objects.get(pk = pk )

	context['state'] = state 

	return render(request, 'state_detail.html', context )

def state_list(request):
	context = {}

	states = State.objects.all() 

	context['states'] = states

	return render(request, 'state_list.html', context ) 

def list(request):
	context = {}
	states = State.objects.all() 
	context['states'] = states 

	return render(request, 'list.html', context)

def detail(request, pk):
	context = {}
	state = State.objects.get(pk=pk)
	context['state'] = state 
	return render(request, 'detail.html', context)

def template_view2(request):
	context={}
	state_city={}

	states = State.objects.all()

	for state in states : 
		cities = state.city_set.filter(name__startswith= 'A')

		state.name = { state.name : cities }
		# push the pair of values in the dictionary
		state_city.update(state.name)
	context['states'] = state_city # the states is the key for the dictionary 

	return render(request, 'base2.html', context )


def template_view(request):
	context = {} #empty dict

	states = State.objects.all()

	context['states'] = states

	return render(request,'base.html', context)


@csrf_exempt
def form_view(request):
	state = request.GET.get('state','D') # fail gracefully
	city = request.GET.get('city','D') # fail gracefully 

	city_state_string = """
		<form action = "/form_view/" method="GET" >

			State : <input type="text" name="state" > <br>
			City: < input type="text" name="city" > <br>

			<input type="submit" value="Submit"> 

		</form>

	"""
	states = State.objects.filter(name__startswith=get_state)

	for state in states:
		cities = state.city_set.filter(name__startswith=get_city) # Parent.child_set [ list of all childs ]
		for city in cities:
			city_state_string += "<b> %s </b> %s  | %s <br>" % (state, city.name, city.zipcode)
	return HttpResponse(city_state_string)

# class GetPost(View):
# 							# keys 	DICT (( i guess )) 
# 	def get(self, request, *args, **kwargs):
# 		city_state_string = """
# 			<form action="/form_view/" method="POST">

# 			State: <input type= "text" name="state" >

# 			<br>

# 			City : <input type ="text" name="city" >

# 			<br>

# 			<input type="submit" value="Search" >

# 			</form>

# 			<br>
# 			<br>

# 			"""
# 			return HttpResponse(city_state_string)

# 	def get(self, request, *args, **kwargs):
# 		get_state = request.POST.get('state', 'c')
# 		get_city = request.POST.get_city('city', 'c')







# get(value,default)
@csrf_exempt
def form_view(request):

# if request.method == 'POST':
	get_state = request.GET.get('state', 'c')
	get_city = request.GET.get('city', 'c')

	city_state_string = """	

	POST: %s <br>
	GET: %s <br>
	META: %s <br>
	<br>

	<form action="/form_view/" method="POST">

	State: <input type= "text" name="state" >

	<br>

	City : <input type ="text" name="city" >

	<br>

	<input type="submit" value="Search" >

	</form>

	<br>
	<br>

	""" % ( escape(request.POST), escape(request.GET), escape(request.META))

	states = State.objects.filter(name__startswith=get_state)

	for state in states:
		cities = state.city_set.filter(name__startswith=get_city)
		for city in cities:
			city_state_string += "<b> %s </b> %s  | %s <br>" % (state, city.name, city.zipcode)
		return HttpResponse(city_state_string)



# we getting all the cities in each state just like 2D array OO

def get_post(request):
	# response = '<--- %s --->' %request.GET 
	# text_string = ''

	# for k , v in request.GET.items()
	# 	print '%s %s' % (k,v)
	# 	text_string += '%s %s <br>' % (k,v)
	
	# 	<-- the idea here is we dont use [''] in the get because it will break the code -->
								#BAD request.GET['blah']

	text_string = ''
	starts_with = request.GET.get('state_name')
	states = State.objects.all().filter(name__startswith=starts_with) 
	for state in states:
			text_string += 'state: %s :) <br>' % (state.name)

	return HttpResponse(text_string)


def first_view(request, starts_with):
	states = State.objects.all()
	text_string = ''
	for state in states:
		cities = state.city_set.filter(name__startswith=starts_with)
		for city in cities:
			print city.zipcode
			text_string += 'state: %s ** city: %s  <br>' % (state.name, city.name)

	return HttpResponse(text_string)



def second_view(request):
	states = State.objects.all()
	text_string = ''
	for state in states:
		cities = state.city_set.filter(name__startswith="M")
		for city in cities:
			text_string += 'state: %s ** city: %s  <br>' % (state.name, city.name)

	return HttpResponse(text_string)


# def state_list(request, letter, sort):
# 	states = State.objects.filter(name__startswith=letter).order_by(sort)
# 	states_list = []

# 	for state in states:
# 		states_list.append('%s <br>' % state.name)

# 	return HttpResponse(states_list)
