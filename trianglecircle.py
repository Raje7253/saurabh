#for area of  triangle 
a=float(input('enter first side :'))
b=float(input('enter second side :'))
c=float(input('enter third side :'))

#for area of circle
radius=float(input('enter the radius of circle :'))


PI = 3.14 # circle pi value

#tringle formula
s=(a+b+c)/2
areatringle=(s*(s-a)*(s-b)*(s-c))**0.5

#circle formula
areacircle=PI*radius*radius
circumference=2*PI*radius

#for output of triangle
print("the area of the triangle is :%0.2f"%areatringle)

#for output of circle
print("area of a circle is : %2f"%areacircle)
print("circumference of circle is : %2f"%circumference)