# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    computor.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/07 19:37:47 by obelouch          #+#    #+#              #
#    Updated: 2020/11/07 20:11:18 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

from srcs.resolver import resolve_deg_2, resolve_deg_1, resolve_deg_0
from srcs.polynome import dict_polynome
import sys


# Errors numbers
ERROR_NO_ARG = -1
ERROR_ARG_NBR = -2
ERROR_FLAG_NBR = -3
ERROR_FLAG = -4
ERROR_SYNTAX_EQUAL = -5
ERROR_SYNTAX_POLY_1 = -6
ERROR_SYNTAX_POLY_2 = -7

# Plot graph flag: -v
is_plot = False
# Show steps in details: -d
is_detail = False

# Dictionary that contain the polynome
polynome = {}


def fill_polynome(p1, p2):
    '''
    fill the dictionary polynome with p1 - p2
    '''
    for degree in p1:
        if degree in polynome:
            polynome[int(degree)] += float(p1[degree])
        else:
            polynome[int(degree)] = float(p1[degree])
    for degree in p2:
        if degree in polynome:
            polynome[int(degree)] -= float(p2[degree])
        else:
            polynome[int(degree)] = -float(p2[degree])


def get_max_degree():
    '''
    Get max degree
    '''
    max_degree = 0
    for degree in polynome:
        if max_degree < degree and polynome[degree] != 0:
            max_degree = degree
    return max_degree


def print_simple_morph(val, degree):
    '''
    Print simple morph for the simple format
    '''
    if val != 0 or degree == 0:
        n = val if val % 1 else int(val)
        if degree == 0:
            print(f'{n}', end="")
        else:
            if (val != 1):
                print(f'{n} * ', end="")
            if (degree != 1):
                print(f'X^{degree}', end="")
            else:
                print(f'X', end="")


def print_reduced_format(max_degree):
    '''
    Print the full + simple reduced format
    '''
    poly = dict(sorted(polynome.items()))
    # Reduced form
    print("Reduced form: ", end="")
    for degree in range(max_degree + 1):
        n = poly[degree] if poly[degree] % 1 else int(poly[degree])
        print(f'{n} * X^{degree}', end="")
        if degree < max_degree:
            print(" + ", end="")
    print(" = 0")
    # Simple form
    if is_detail:
        print("Simple form: ", end="")
        for degree in range(max_degree + 1):
            print_simple_morph(poly[degree], degree)
            if degree < max_degree and poly[degree] != 0:
                print(" + ", end="")
        print(" = 0")


def print_result(max_degree):
    '''
    Print the result of the equation
    '''
    print_reduced_format(max_degree)
    print(f"Polynomial degree: {max_degree}")
    if max_degree > 2:
        print("The polynomial degree is stricly greater than 2, I can't solve.")
    elif max_degree == 2:
        resolve_deg_2(polynome,is_detail,is_plot)
    elif max_degree == 1:
        resolve_deg_1(polynome,is_detail,is_plot)
    else:
        resolve_deg_0(polynome)


def dict_rebuild(max_degree):
    '''
    Rebuild the dictionary by filling the missing fields with 0
    '''
    for i in range(max_degree + 1):
        if i not in polynome:
            polynome[i] = 0


def get_flags_args(argv):
    '''
    Check & Get the flags, argument from argv
    '''
    global is_plot
    global is_detail
    flags = [arg for arg in argv if len(arg) == 2 and arg[0] == '-']
    args = [arg for arg in argv if arg not in flags]
    if (len(flags) > 2):
        return ERROR_FLAG_NBR
    for flag in flags:
        if (flag == '-v'):
            is_plot = True
        elif (flag == '-d'):
            is_detail = True
        else:
            return ERROR_FLAG
    if (len(args) == 1):
        return ERROR_NO_ARG
    if (len(args) != 2):
        return ERROR_ARG_NBR
    return args[1]


def exit_usage(error):
    '''
    Print the usage & msg error then exit
    '''
    if (error == ERROR_NO_ARG):
        print('Error: No argument!')
    elif (error == ERROR_ARG_NBR):
        print('Error: Wrong number of arguments!')
    elif (error == ERROR_FLAG):
        print('Error: Wrong used flag!')
    elif (error == ERROR_FLAG_NBR):
        print('Error: More than 2 flags are used')
    elif (error == ERROR_SYNTAX_EQUAL):
        print('Error: Equal sign doesn\'t exist in the eqution!')
    elif (error == ERROR_SYNTAX_POLY_1):
        print('Error: Syntax Error in the first polynome!')
    elif (error == ERROR_SYNTAX_POLY_2):
        print('Error: Syntax Error in the second polynome!')
    else:
        print('Syntax Error!')
    print('Usage: ./computor [-v][-d] < equation >')
    print('          equation: < polynome1 > = < polynome2 >')
    print('          -v: Plot the result when it make sense')
    print('          -d: Print Steps in details')
    exit(1)


def comp_v1():
    arg = get_flags_args(sys.argv)
    # Check the arg returned that can contain the argument or an error number
    if (type(arg) != str):
        exit_usage(arg)
    str_polys = arg.split('=')
    if (len(str_polys) != 2):
        exit_usage(ERROR_SYNTAX_EQUAL)
    p1 = dict_polynome(str_polys[0])
    p2 = dict_polynome(str_polys[1])
    # Check if the polynomes are correct:
    if (not p1):
        exit_usage(ERROR_SYNTAX_POLY_1)
    if (not p2):
        exit_usage(ERROR_SYNTAX_POLY_2)
    fill_polynome(p1, p2)
    max_degree = get_max_degree()
    dict_rebuild(max_degree)
    print_result(max_degree)


comp_v1()
