from geometry.geometry import Layer, snell
import matplotlib.pyplot as plt
import numpy as np

air1 = Layer({
    'input' : 0,
    'refraction' : 1
})

air2a = Layer({
    'input' : 5,
    'refraction' : 1
})

air2b = Layer({
    'input' : -5,
    'refraction' : 1
})

polia = Layer({
    'input' : -5,
    'refraction' : 1.585
})

polib = Layer({
    'input' : 5,
    'refraction' : 1.585
})

glass = Layer({
    'input' : 0,
    'refraction' : 1.52
})

xa = []
ya = []

xb = []
yb = []

xc = []
yc = []

for i in range(0, 90):
    first_ref = snell(i, air1, polia)[0]
    second_ref = snell(first_ref, polia, air2a)[0]
    third_ref = snell(second_ref, air2a, glass)[0]
    xa.append(i)
    ya.append(third_ref)
    print("r0: {:.2f}\tr1: {:.2f}\tr2: {:.2f}\tr3: {:.2f}".format(i ,first_ref, second_ref, third_ref))

for i in range(0, 90):
    first_ref = snell(i, air1, polib)[0]
    second_ref = snell(first_ref, polib, air2b)[0]
    third_ref = snell(second_ref, air2b, glass)[0]
    xb.append(i)
    yb.append(third_ref)
    print("r0: {:.2f}\tr1: {:.2f}\tr2: {:.2f}\tr3: {:.2f}".format(i ,first_ref, second_ref, third_ref))

for i in range(0, 90):
    first_ref = snell(i, air1, glass)[0]
    second_ref = snell(first_ref, glass, air1)[0]
    third_ref = snell(second_ref, air1, glass)[0]
    xc.append(i)
    yc.append(third_ref)
    print("r0: {:.2f}\tr1: {:.2f}\tr2: {:.2f}\tr3: {:.2f}".format(i ,first_ref, second_ref, third_ref))


fig, ax = plt.subplots()
h1 = ax.plot(xa, ya, label='variant A')
h2 = ax.plot(xb, yb, label='variant B')
h3 = ax.plot(xc, yc, label='standard plate')
ax.grid(True)
plt.title("Refraction Result")
plt.xlabel(r'input($\beta_1$)')
plt.ylabel(r'output($\beta_2$)')
plt.legend()
plt.show()