#patterns

# # # #
# # # #
# # # #
# # # #

#program

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
print()



#
# #
# # #
# # # #

#program

for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
print()



# # # #
# # #
# #
#

#program

for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
print()

    #
  #   #
 #  #   #
#  #   #  #

n=4
for i in range(4):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(" # ",end=" ")
    print()

print()




 #   #   #   #
   #   #   #
     #   #
       #
p=4

for i in range(4):
    for j in range(i):
        print(" ",end=" ")
    for k in range(p-i):
        print(" # ",end=" ")
    print()