# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    libmath.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/07 19:36:55 by obelouch          #+#    #+#              #
#    Updated: 2020/11/07 19:37:08 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def max(a, b):
    if (a > b):
        return a
    return b


def min(a, b):
    if (a < b):
        return a
    return b


def print_float(x, i=0):
    print(x, end="") if x % 1 else print(int(x), end="")
    if (i < 0):
        print(f' - {-i}*i', end="") if i % 1 else print(f' - {int(-i)}*i', end="")
    elif (i > 0):
        print(f' + {i}*i', end="") if i % 1 else print(f' + {int(i)}*i', end="")
    print("")