'''
names = {"Sagar", "SAGAR", "SaGaR", "sAGAR", "SAgAR"}
name = input("Enter the Name to Check: ")
if name in names:
    print("Talk About Sagar")
else:
    print("Talk not about Sagar")
'''
post = input("Post: ")

if("Sagar" in post or "SAGAR" in post or "sagar" in post or "SaGaR" in post):
    print("Post in talking about me")
else:
    print("Post isn't talking about me")
