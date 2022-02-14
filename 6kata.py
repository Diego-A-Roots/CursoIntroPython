planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(len(planets), 'el ultimo es ' + planets[7])

#////////////////////////////////////////////////////

planeta = input('escriba el nombre de un planeta ')

buscar = planets.index(planeta)

print('aqui se muestra los planetas mas cercanos de ' + planeta)
print(planets[0:buscar])

print('aqui los planetas mas lejanos al sol ' + planeta)
print(planets [buscar + 1:])