rooms = ["room1","room2","washroom","room4"]
roomnames = {"room1":"drawingroom","room2":"kitchen","room3":"bedroom","room4":"gamingroom"}
value = "washroom"
for room in rooms:
    if room == value:
        print("ma clean nahi karo ga ganda ha ya")
        continue
    else:
        print("cleaned " + room)
print("end of loop")