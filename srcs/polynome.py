# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    polynome.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/07 20:01:44 by obelouch          #+#    #+#              #
#    Updated: 2020/11/07 20:03:09 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re

# Regex patterns
regx = [
    '^-?([0-9]+(\\.?[0-9]+)?\\*)?[xX]\\^[0-9]+$',
    '^-?([0-9]+(\\.?[0-9]+)?\\*)?[xX]$',
    '^-?[0-9]+(\\.?[0-9]+)?$',
]

def append_to_dict(semi_poly, val, degree):
    '''
    append to dictionary if the key exist or not 
    '''
    if int(degree) in semi_poly:
        semi_poly[int(degree)] += float(val)
    else:
        semi_poly[int(degree)] = float(val)


def morphs_to_dict(morphs):
    '''
    Create the dictionary for the polynome given as list of morphs
    '''
    semi_poly = {}
    for morph in morphs:
        nums = 0
        if re.search(regx[0], morph):
            nums = re.findall('-?\\d+\\.\\d+|-?\\d+', morph)
            if len(nums) == 1:
                nums.insert(0, -1 if morph[0] == '-' else 1)
            append_to_dict(semi_poly, nums[0], nums[1])
        elif re.search(regx[1], morph):
            nums = re.findall('-?\\d+\\.\\d+|-?\\d+', morph)
            if len(nums) == 0:
                nums = [-1 if morph[0] == '-' else 1, 1]
            append_to_dict(semi_poly, nums[0], 1)
        elif re.search(regx[2], morph):
            nums = re.findall('-?\\d+\\.\\d+|-?\\d+', morph)
            append_to_dict(semi_poly, nums[0], 0)
        else:
            return False
    return semi_poly


def dict_polynome(str_poly):
    '''
    string polynome ----> dictionary polynome
    '''
    poly = ''.join(str_poly.split()).replace(
        '--', '+').replace('-+', '-').replace('+-', '-').replace('-', '+-')
    morphs = poly.split('+')
    morphs = morphs[1:] if morphs[0] == "" else morphs
    return morphs_to_dict(morphs)