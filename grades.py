name = input("Input student name >>")
sub1 = int(input(f"{name}'s Math marks :"))
sub2 = int(input(f"{name}'s English marks :"))
sub3 = int(input(f"{name}'s Kiswahili marks :"))
sub4 = int(input(f"{name}'s Science marks :"))
sub5 = int(input(f"{name}'s Social Studies marks :"))
sub6 = int(input(f"{name}'s C.R.E marks :"))
total = sub1+sub2+sub3+sub4+sub5+sub6
print("Total Score: ",total)
percentage = float(total/600) * 100
print("Percentage= ",percentage,"%")