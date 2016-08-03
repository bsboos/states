#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State,City

import django
django.setup()

#State.objects.all().delete()

#WE ONLY WANT THE DIRECTORY NAME, NOT THE FILE. THIS SHOWS THE FILE: print os.path.abspath(__file__)

#THIS STOPS AT THE DIRECTORY THE FILE IS AT: print os.path.dirname(os.path.abspath(__file__))

#THIS IS WRONG BECAUSE IT ONLY WORKS WITH MACS: print "%s/states.csv" % os.path.dirname(os.path.abspath(__file__))

# THIS IS THE CORRECT WAY TO PRINT THE PATH: print os.path.join(os.path.dirname(os.path.abspath(__file__)), "states.csv")

#print os.path.join("one", "two", "three")

csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zip_codes_states.csv")

csv_file = open(csv_path, 'r') #'r' means read. 

reader = csv.DictReader(csv_file) # This is for the python dictionary to read the file


for row in reader: # this is for us to add the states into the database.
	state, created = State.objects.get_or_create(abbreviation=row['state'])

	try:
		new_city, created = City.objects.get_or_create(latitude=row['latitude'])

		new_city.state= state 
		new_city.name = row['city']
		new_city.county = row['county']
		new_city.longitude = row['longitude']
		new_city.zipcode = row['zip_code']
		new_city.save()

		print new_city.name

	except Exception, e:
		print e 
