import graphics.rectangle
print("Rectangle")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("Area of rectangle: ",graphics.rectangle.area(l,b))
print("Perimeter of rectangle: ",graphics.rectangle.perimeter(l,b))

from graphics.circle import area
from graphics.circle import perimeter as p
print("***************************")
print("Circle")
r=int(input("Enter the radius:"))
print("Area of circle: ",area(r))
print("Perimeter of circle: ",p(r))



from graphics.dgraphics.cuboid import area as a
from graphics.dgraphics.cuboid import perimeter as p
print("*****************************")
print("Cuboid")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
h=int(input("Enter the height:"))
print("Total surface area: ",a(l,b,h))
print("Perimeter : ",p(l,b,h))


from graphics.dgraphics.sphere import *
print("****************************")
print("Sphere")
r=int(input("Enter the radius:"))
print("Surface area: ",area(r))
print("Circumference : ",circumference(r))
