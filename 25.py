sub1 = int(input("Enter First Subject Marks: "))
sub2 = int(input("Enter Second Subject Marks: "))
sub3 = int(input("Enter Third Subject Marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("\nYou Are Fail because you have less then 33% marks in one of the subject.")
elif(sub1+sub3+sub3)/3 <40:
    print("\nYou are fail due to total percentage less then 40%")
else:
    print("\nCongratulations! You are Passed...")