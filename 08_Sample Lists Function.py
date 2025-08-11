
Food_menu = ["burger","spaghetti","chicken","ice cream"] #list and elements
Food_menu [3] = "spaghetti"  #change the item at index 3 to "spaghetti"
print (Food_menu [3]) #print the value at index 3, which is now "spaghetti"
print("\n") #line break/space

Food_menu = ["burger","spaghetti","chicken","ice cream"] #list and elements

print (Food_menu [1:3]) # means: take elements at index 1 and 2, but not index 3 because index 3 is the stopping point, not included.
print("\n") #line break/space

lucky_numbers = [1,2,3,4,5,6,7,8,9,10]
plants = ["begonia","lily","carnation","tulip","violet","crocus","carnation","carnation"]
lucky_numbers.extend(plants) #it will print the extension or add another lists to combine.
lucky_numbers.append(1111) #add another element of list / additional item at the end.
plants.insert(2,"waterlily") # add element in the middle of the lists
plants.remove("crocus") # remove element from the lists
lucky_numbers.clear() # it will clear or delete all the elements inside the list
plants.pop() # it removes the last element from the list
print (plants.index("carnation"))  # it will determine the index of the element. NOTE: It will give an error if it's not in the list.
print (plants.count("carnation"))  # it will count how many carnation in the list
plants.sort() # print in ascending alphabetical order.
plants.reverse() # print in reverse from the right(last element) to left(first element)
unlucky_numbers = lucky_numbers.copy() # it will copy all the elements from list.
print (unlucky_numbers)
