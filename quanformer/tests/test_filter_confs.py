"""
test_filter_confs.py
"""
import sys
import os
import pytest

# define location of input files for testing
mydir = os.path.dirname(os.path.abspath(__file__))

# import functions to aid testing
sys.path.append(os.path.join(os.path.dirname(__file__), 'helpers'))
from helper import *

from quanformer.filter_confs import *

# -----------------------

def test_identify_minima():
    mols = read_mol(os.path.join(mydir, 'data_tests', 'gbi.sdf'), True)
    mol = next(mols)
    assert mol.NumConfs() == 36
    # use same params defined in filter_confs.py script
    assert identify_minima(mol, 'MM Szybki SD Energy', 5.E-4, 0.2) is True
    assert mol.NumConfs() == 5


def test_filter_confs():
    filter_confs(
        os.path.join(mydir, 'data_tests', 'gbi.sdf'), 'MM Szybki SD Energy',
        'output.sdf')
    mols = read_mol(os.path.join(os.getcwd(), 'output.sdf'), True)
    mol = next(mols)
    assert mol.NumConfs() == 5
    os.remove(os.path.join(os.getcwd(), 'output.sdf'))
    os.remove(os.path.join(os.getcwd(), 'numConfs.txt'))


# test manually without pytest
if 0:
    test_identify_minima()
    test_filter_confs()
