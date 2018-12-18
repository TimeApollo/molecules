#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Molecule max area finder.

Program takes in sets of 4 strings of 12 upper case letters and
determines the best combination to get the max area made by
the rectangle they form by matching letters in their strings as
intersections.

Author: Aaron Jackson, Travis Anderson
Github: TimeApollo, Tander29
"""
__author__ = "Aaron Jackson and Travis Anderson"

import argparse
from itertools import permutations


def mol_permutation(mol_group):
    """Returns list of all possible permutations."""

    perm = permutations([mol_group[0], mol_group[1],
                         mol_group[2], mol_group[3]])
    perm_list = list(perm)
    return perm_list


def find_largest_area(mol_groups, pos_combos):
    """Finds largest area for each group in mol_groups using pos_combos."""
    """
    Iterate over molecule groups.
    Iterate over each tulple combo.
    Iterate over each permutation.
    Iterate over each molecule string in 4 stack loop.
        check if match to continue further into loop hell.
        else break
            if all match print area
    if no match for all loops break from tuple combo and print 0.
    move to next group.
    end if line starts with Q
    """
    for mol_group in mol_groups:
        """Get group of 4 molecules from list and permutations for group."""
        if len(mol_group) == 1:
            break
        valid = False
        mol_perms = mol_permutation(mol_group)
        for pos_combo in pos_combos:
            """Pos combos is biggest area first, looking for smaller area,
            cooridinates are a range """
            for mol_perm in mol_perms:
                """Mol Perms were found, now looping through each perm
                to see if box exists."""
                valid = check_for_valid_combo(pos_combo, mol_perm)
                if valid:
                    print(pos_combo[2])
                    break
            if valid:
                break
        if not valid:
            print(0)


def check_for_valid_combo(pos_combo, mol_perm):
    """Compares a single combo(range of potential coordinates)
    to a single permutation"""
    # need to subtract 1 to only account for gap and not include endpoint
    x_gap, y_gap = pos_combo[0] - 1, pos_combo[1] - 1
    s1, s2, s3, s4 = mol_perm
    # Loops over s1 for possible first intersection comparing s1 to s2.
    for i_s1 in range(1, 11 - x_gap):
        # Loops over second string and intersections with first, s1 s2
        for i_s2 in range(1, 11 - y_gap):
            # test if first intersection is equal, s1, s2, if equal continue.
            if s1[i_s1] == s2[i_s2]:
                # Loops over third string and intersections with second, s2 s3
                for i_s3 in range(1, 11 - x_gap):
                    # if intersection is equal, s2, s3, continue.
                    if s2[i_s2 + y_gap] == s3[i_s3]:
                        # if 3 previous intersections are true,
                        # loop over s4 for possible intersections.
                        for i_s4 in range(1, 11 - y_gap):
                            # compare s4 to s3/s1 with gap
                            if (s1[i_s1 + x_gap] == s4[i_s4]
                               and s3[i_s3 + x_gap] == s4[i_s4 + y_gap]):
                                return True
    return False


def combination_tuple():
    """Returns list of tuples for combos from biggest to smallest area.
    , coordinates are a range"""
    combos = []
    for i in range(3, 11):
        counter = 10
        while counter > 2:
            combos.append((i, counter, (i*counter)-(2*i)-(2*(counter-2))))
            counter -= 1
    combos = sorted(combos, key=lambda x: x[2], reverse=True)
    return combos


def group_molecules(mol_list):
    """Takes list of molecules and splits into 4's to feed into code."""
    group_mol = []
    group_size = 4
    for i in xrange(0, len(mol_list)-1, group_size):
        group_mol.append(mol_list[i:i + group_size])
    group_mol.append(mol_list[-1])
    return group_mol


def read_file(mol_file):
    """Reads molecule file lines."""
    with open(mol_file, 'r') as f:
        return f.read().split('\n')


def create_parser():
    """Creates Parser to pull in file provided."""
    parser = argparse.ArgumentParser(description='Provide molecule file')
    parser.add_argument('file', help='Include filename to run')
    return parser


def main():
    """Runs molecule implementation."""
    parser = create_parser().parse_args()

    mol_list = read_file(parser.file)
    groups = group_molecules(mol_list)
    possible_combinations = combination_tuple()
    find_largest_area(groups, possible_combinations)


if __name__ == "__main__":
    main()
