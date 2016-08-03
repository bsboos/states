#!/usr/bin/env python
import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

from app.models import State

import django
django.setup()


#states = State.objects.all().order_by('capital')

#states = State.objects.all().exclude(name__startswith="c").order_by('name')

#states = State.objects.all().filter(name__startswith="c").order_by('name')

#OBJECTS TAKE UP A LOT OF THE MEMORY, THAT'S WHY WE WILL RUN THE DICTIONARY BELOW INSTEAD OF THE WHOLE OBJECT (WHICH IS ABOVE).

#states = State.objects.all().values('name', 'population')

# A LIST (BELOW) IS EVEN EASIER


states = State.objects.all().values_list('name', 'abbreviation', 'population')


#THIS WILL PRINT LIST BELOW EACH OTHER.
#for a, b, c in states:
#	print a
#	print b
#	print c

for state in states:
	print state


#for state in states:
#	print "%s | %s | %s" % (state.name, state.capital, state.population)





