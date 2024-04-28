#11
print("11. ",list(range(-1,11,11)))

#12
x=3
if x<0:
   print("12. True")
else:
   pass
   print("12. Empty Screen")

#13
'''
x=[12,33,"44',55,66,]
print(x[0])
'''
print("13. Error")

#14
x=[12,33,44,55,66,77]
print("14. ",x[-2:-4])

#15
x=[[12,33],55,52,85,99]
print("15. ",x[-5][-2])

#16
x=3
if x>0:
  pass
  print("16. Empty Screen")
else:
  print("16. Hello world")

#17
x=[12,33,44,44]
x.insert(2,[90,78,54])
print("17. ",x[2][-2])

#18
x=[66,66,66,66,66,66]
x.remove(66)
print("18. ",x)

#19
x=[12,33,[89,4,22],77,32]
print("19. ",len(x))

#20
x=[12,33,44,32,11,22]
print("20. ",sum(x[-1:-3]))

#21
x=[12,12,12,12]
x.pop()
print("21.",x)

#22
x=[12>90,3,90<99]
print("22. ",x[-1])

#23
print("23. ",list(range(10,2,10)))

#24
x=[10]*5
print("24. ",x)

#25
if "a":
   print("25. 0")
else:
   print("25. 1")
