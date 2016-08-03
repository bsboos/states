#!/usr/bin/env python
import csv
import os
import sys
import django

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State, StateCapital

states = State.objects.all() 

django.setup()

#State.objects.all().delete()

#WE ONLY WANT THE DIRECTORY NAME, NOT THE FILE. THIS SHOWS THE FILE: print os.path.abspath(__file__)

#THIS STOPS AT THE DIRECTORY THE FILE IS AT: print os.path.dirname(os.path.abspath(__file__))

#THIS IS WRONG BECAUSE IT ONLY WORKS WITH MACS: print "%s/states.csv" % os.path.dirname(os.path.abspath(__file__))

# THIS IS THE CORRECT WAY TO PRINT THE PATH: print os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.csv")

#print os.path.join("one", "two", "three")

csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.csv")

csv_file = open(csv_path, 'r') #'r' means read. 

reader = csv.DictReader(csv_file) # This is for the python dictionary to read the file

State.objects.all().delete()
for row in reader: # this is for us to add the states into the database.

	#new_state = State()

	new_state, created = State.objects.get_or_create(abbreviation=row['abbrev'])

	new_state.abbreviation = row['abbrev']
	new_state.name = row['state']

	new_state.save()


	new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])

	new_capital.state = new_state #this references the row in our database (states.csv), it displays the id because it is unique. We could have duplicate 'names' but not duplicate id's. 
	new_capital.latitude = row['latitude']
	new_capital.longitude = row['longitude']
	new_capital.population = row['population']

	new_capital.save()

