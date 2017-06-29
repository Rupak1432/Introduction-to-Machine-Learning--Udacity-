#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
"""
print(enron_data["SKILLING JEFFREY K"]["total_payments"])
print(enron_data["FASTOW ANDREW S"]["total_payments"])
#print(enron_data["KRAUTZ MICHAEL"])
"""
s= 0
e =0
c = 0
for key in enron_data:
	#if (enron_data[key]["salary"] != 'NaN'):
	#	s += 1
	#if (enron_data[key]["email_address"] != 'NaN'):
	#	e+=1
	if (enron_data[key]["total_payments"] == 'NaN'):
		c += 1 

	if (enron_data[key]["poi"] == True):
	#	print(key)
		e += 1
		if (enron_data[key]["total_payments"] == 'NaN'):
			s += 1 

print(float(s)/float(e))
print(s)
print(e)
print(c)


