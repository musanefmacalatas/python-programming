
#Useful for storing fixed data that should not be changed, like coordinates.
#creating tuples
rgb_colors = ('RED', 'GREEN', 'BLUE')
rgb_colors = rgb_colors[::-1] # reverse the elements arrangement from value -1
print(rgb_colors)
print(rgb_colors[0])
print(rgb_colors[1])

print("\n")

rgb_colors = ('RED', 'GREEN', 'BLUE','RED')
print(rgb_colors.count('RED'))  # Output: 2
print(rgb_colors)

print("\n")

info = ( 'Nef' , 30 , 'Philippines')
print(info[0])
print(info[1])
print(info[2])
print("\n")
locations = {                             #dictionary
    (14.5995, 120.9842): "Manila",       #key : value (coordinates longitude and latitude : location)
    (35.6895, 139.6917): "Tokyo"
}
print(locations[14.5995, 120.9842])
print(locations[35.6895, 139.6917])




