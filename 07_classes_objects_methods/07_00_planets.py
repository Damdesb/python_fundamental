'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

# class Planet():
#     pass

# fix the code so it works as expected


name = "Mycroft"

def print_name_box():
  print(name)

  def smaller_box():
    '''
    (re)assigning a variable within the same scope
    overwrites the same variable from an outer scope
    -> you cannot use it *before* assigning it,
    if you assign it at all anywhere in that scope.
    --TASK--: uncomment the below print() statement
        and interpret the results when running it
    '''

    #print(name)
    name = "Sherlock"

    def smallest_box():
      '''
      inner scopes always draw from the next-outer layer
      after 'name' got overwritten, the name that will
      be printed is NOT the global-scope name anymore
      '''

      print(name)

    smallest_box()

  smaller_box()

print_name_box()