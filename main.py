from geometry.geometry import Layer, snell
import matplotlib.pyplot as plt
import numpy as np

air = Layer({
    'input' : 0,
    'refraction' : 1
})

poli = Layer({
    'input' : -5,
    'refraction' : 1.5
})

glass = Layer({
    'input' : 0,
    'refraction' : 1.2
})

x = []
y = []

for i in range(45, 85):
    first_ref = snell(i, air, poli)[0]
    second_ref = snell(first_ref, poli, air)[0]
    third_ref = snell(second_ref, air, glass)[0]
    x.append(i)
    y.append(third_ref)
    print("r0: {:.2f}\tr1: {:.2f}\tr2: {:.2f}\tr3: {:.2f}".format(i ,first_ref, second_ref, third_ref))

fig, ax = plt.subplots()
ax.plot(x, y)
plt.title("Refraction Result")
plt.xlabel(r'input($\beta_1$)')
plt.ylabel(r'output($\beta_2$)')
plt.show()