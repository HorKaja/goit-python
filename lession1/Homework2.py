# prompt user to input all coeficients of quadratic equation
print("The quadratic equation a * x ^ 2 + b * x + c = 0 will be solved after input of coeficients below :")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
# calculate discriminant
d = b ** 2 - 4 * a * c
# calculate both equation roots
x1 = (-b + d ** 0.5)/(2*a)
x2 = (-b - d ** 0.5)/(2*a)
# output of solutions
if d > 0:
    print("x1 = ", x1, "; x2= ", x2)
if d == 0:
    print("x1 = ", x1)
# legal clause in case we crashed someone's brain
else:
    print("...Your school teachers have been lying to you all that time! Even though the discriminant is below zero,\n",
          "there is a secret solution to this equation represented as complex numbers.\n",
          "However, if you use this app to solve your school homework, you better indicate there is no solution!\n",
          "We are not liable for any unintended consequences... So here we go: \n",
          "x1= ", x1, "; x2= ", x2, "\n"
          "If you enjoyed using this app, you may want to donate 1$ (card N 51687559395987161)")
