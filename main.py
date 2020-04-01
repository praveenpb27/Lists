.replit
#List demonstration
myList = ["List item 1", 2, 3.14]
print('List is', myList[0:5])

#changing a value within list 
myList[0] = 'New item 2' # List values can be updated
print('Updated List items are', myList[0:5])


#Tuple demonstration
print ('\n-------------')
myTuple = (1,2,"Tuple",3,14)
print ('Tuples are', myTuple)
#printing first tuple item
print ('First tuple is ', myTuple[0])
#Trying to change a value within Tuple 
#myTuple[0] = 11  //*** Not-Possible becoz Tuple datatype is immutable i.e., once assigned the values can't be updated ****
#print ('Updated First Tuples is', myTuple[0])


#Dictonary demonstration
print ('\n-------------')
myDict = {'PI': 3.14,
          'ID': 123,
          'City': 'London',3:33
         }
print('Dictionary items are', myDict)
print('Tuple item PI value is', myDict['PI'])
print ('Printing a dict value', myDict['PI'])
#changing a value within dict items
myDict ['PI'] = 4.14 # dict values can be updated
print ('Printing new dict value', myDict['PI'])