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

    return


def combination_tuple():
    """Returns list of tuples for combos from biggest to smallest area."""
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
