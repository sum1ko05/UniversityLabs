# from space2d import Vector2d, Vector3d
from point2d import Point2d
from vector2d import Vector2d
from vector3d import Vector3d

# Point test
# Error will be called here if position is out of range
p1 = Point2d(1000, 0)
p2 = Point2d(800, 0)
print(p1, p2, p1 == p2)
print(repr(p1))

# Vector test
v12 = Vector2d(3, 4)
print(v12, abs(v12))
v22 = Vector2d(2, 6)
vsum2 = v12 + v22
vsub2 = v12 - v22
print(vsum2, vsub2)
v12 = v12 * 5
print(v12)
v12 = v12 / 5
print(v12, v22)
scalar = v12.scalar_product(v12)
print("scalar: ", scalar)
for coord in v22:
    print(coord)
print("by variables: ", v22.x, v22.y)
print("by indices: ", v22[0], v22[1])
v30 = Vector3d.vector_product(Vector3d.from_vector2d(v12), Vector3d.from_vector2d(v22))
print(v12, v22, v30)
print(Vector3d(1, 2, 3) + Vector3d(4, 3, 2))

length = 10
width = 5
height = 2
vlen = Vector3d(length, 0, 0)
vwid = Vector3d(0, width, 0)
vhei = Vector3d(0, 0, height)
volume = abs(Vector3d.triple_product(vlen, vwid, vhei))
print(length, width, height, volume)
