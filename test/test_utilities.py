import pytest

import theano
import numpy as np
import sys, os
sys.path.append("../..")
import gempy as gp
import matplotlib.pyplot as plt
import pdb



input_path = os.path.dirname(__file__)+'/../notebooks'

def test_set_orientations():
    # Importing the data from CSV-files and setting extent and resolution
    geo_data = gp.create_data([0, 2000, 0, 2000, 0, 2000], [50, 50, 50],
                              path_o=input_path+'/input_data/tut_chapter1/simple_fault_model_orientations.csv',
                              path_i=input_path+'/input_data/tut_chapter1/simple_fault_model_points.csv')


    gp.get_data(geo_data)

    # Assigning series to formations as well as their order (timewise)
    gp.set_series(geo_data, {"Fault_Series":'Main_Fault',
                             "Strat_Series": ('Sandstone_2','Siltstone',
                                              'Shale', 'Sandstone_1')},
                           order_series = ["Fault_Series", 'Strat_Series'],
                           order_formations=['Main_Fault',
                                             'Sandstone_2','Siltstone',
                                             'Shale', 'Sandstone_1',
                                             ], verbose=0)

    gp.set_orientation_from_interfaces(geo_data, [0, 1, 2])
