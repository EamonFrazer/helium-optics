from geometry.geometry import Layer

layer = Layer({
    'input' : -5,
    'output' : 0,
    'refraction' : 1.5
})

for i in range(45, 90):
    print("input: {:.2f}, output: {:.2f}".format(i, layer.proc(i)['b4']))