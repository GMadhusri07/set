# 2. Take a set of no,take elements from the user, remove that element  from the existing set  and store in the new set
myset={1,3,4,5,6,7,9,0}
newset=set()
total_inputs=4
for i in range(1,total_inputs+1,1):
  user_input=int(input("enter a number from the myset :"))
  if user_input in myset:
     myset.remove(user_input)
     newset.add(user_input)
  else:
     print(user_input, "not in myset")
print("newset now contains :", newset)

#  ----------------------------------------------------------------------------------------------------------------------

# Check whether the below methods are working for set or not. i.e. issubset(),issuperset(),isdisjoint()

set={1,3,4,5,6,7,9,0}
set2={2,3,4}
print(set.isdisjoint(set2))
print(set2.issubset(set))
print(set.issuperset(set2))

# output:
# False
# False
# False
# note: issubset(), issuperset(),isdisjoint() works for set also