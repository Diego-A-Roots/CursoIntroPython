from turtle import done


new_planet = ''
planets = []

while new_planet != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('escribe un nuevo planeta 0 done para salir   ')

for planet in planets:
    print(planet)

#///////////////////////////////////////////////////////////////////////

