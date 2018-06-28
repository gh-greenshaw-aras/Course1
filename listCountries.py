# listCountries.py

from artiom import getListOfCountries
from christopher import getCapitalCity
from mayurapiriyan import getArea
from noor import getPopulation
from ruth import getCurrency
from simon import getDialingCode 

print('Available countries are:\n' + getListOfCountries())

print('The capital city of Nepal is ' + getCapitalCity('Nepal'))
print('The currency in Cambodia is the ' + getCurrency('cambodia'))
print('The area in square kilometres of Egypt is ' + getArea('Egypt'))
print('The population of The Philippines is ' + getPopulation('Philippines'))
print('The dialing code for Bulgaria is ' + getDialingCode('Bulgaria'))
#print('The population density of The Philippines is ' + getPopulationDensity('Philippines') + ' per square kilometre')

