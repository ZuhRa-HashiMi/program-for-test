gal_moon={'io':'182.21', 'Euop':'1560.8'}
moon_surface={'io':'1.796', 'Euop':'1.314'}
moon_orbital={'io':'1.769', 'Euop':'3.551'}
print('which property do you want:')
for moon in gal_moon:
    print(moon)
property=input(':')

print(gal_moon.get(property))
print(moon_surface.get(property))
print(moon_orbital.get(property))


print('HELLO ZUHARA ');

