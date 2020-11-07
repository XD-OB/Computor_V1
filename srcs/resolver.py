# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    resolver.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/07 19:50:19 by obelouch          #+#    #+#              #
#    Updated: 2020/11/07 20:22:58 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from    srcs.plot import poly_plot_deg_2, poly_plot_deg_1
from    srcs.libmath import print_float

def resolve_deg_2(polynome,is_detail,is_plot):
    '''
    Solve Equation second degree
    '''
    x = []
    delta = (polynome[1] ** 2) - (4 * polynome[0] * polynome[2])
    if is_detail:
        print("\nWe can write this polynome as follow: a * X^2 + b * X + c = 0")
        print(
            f"with: a = {polynome[2]} , b = {polynome[1]} , c = {polynome[0]}")
        print("to solve this equation first we calculate the Polynomial discriminant:")
        print(" delta = b^2 - 4*a*c")
        print("       =", delta,)
    if (delta > 0):
        x.append((- polynome[1] + delta ** (0.5))/(2 * polynome[2]))
        x.append((- polynome[1] - delta ** (0.5))/(2 * polynome[2]))
        print("Discriminant is strictly positive, the two solutions are:")
        if is_detail:
            # first solution
            print("x1 = (-b + sqrt(delta)) / (2 * a)")
            print(f"   = ({-polynome[1]} + sqrt({delta})) / {2 * polynome[2]}")
            print("   = ", end="")
            print_float(x[0])
            # second solution
            print("x2 = (-b - sqrt(delta)) / (2 * a)")
            print(f"   = ({-polynome[1]} - sqrt({delta})) / {2 * polynome[2]}")
            print("   = ", end="")
            print_float(x[1])
        else:
            print_float(x[0])
            print_float(x[1])
    elif (delta == 0):
        x.append((- polynome[1])/(2 * polynome[2]))
        print("Discriminant is Null, the solution is:")
        if (is_detail):
            print("x = -b / (2 * a)")
            print(f"  = ({-polynome[1]} / {2 * polynome[2]})")
            print("  = ", end="")
        print_float(x[0])
    else:
        r = (- polynome[1])/(2 * polynome[2])
        i = (-delta)**(0.5)/(2 * polynome[2])
        print("Discriminant is strictly negative, the two solutions are:")
        if (is_detail):
            # first solution
            print("x1 = (-b + i * sqrt(-delta)) / (2 * a)")
            print("   = ", end="")
            print_float(r, i)
            # second solution
            print("x2 = (-b - i * sqrt(-delta)) / (2 * a)")
            print("   = ", end="")
            print_float(r, -i)
        else:
            print_float(r, i)
            print_float(r, -i)
    if is_plot:
        if delta >= 0:
            poly_plot_deg_2(polynome, x)
        else:
            print("No meaning from ploting Complex Solutions")


def resolve_deg_1(polynome,is_detail,is_plot):
    '''
    Solve Equation first degree
    '''
    x = -polynome[0] / polynome[1]
    if (is_detail):
        print("\nWe can write this polynome as follow: a * X + b = 0")
        print(f"with: a = {polynome[1]} , b = {polynome[0]}")
        print("the solution is x:")
        print(f"x = - b / a\n  = {-polynome[0]} / {polynome[1]}\n  = ", end="")
        print_float(x)
    else:
        print("The solution is:")
        print_float(x)
    if is_plot:
        poly_plot_deg_1(polynome, x)


def resolve_deg_0(polynome):
    '''
    Solve Equation zero degree
    '''
    if (polynome[0] == 0):
        print("All the real numbers are solution")
    else:
        print("There are no solutions")