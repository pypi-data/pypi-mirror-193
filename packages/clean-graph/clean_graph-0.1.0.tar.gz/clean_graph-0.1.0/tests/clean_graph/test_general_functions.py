"""test General functions."""

from clean_graph.general_functions import *
import pytest

# # Import modules
# import matplotlib.pyplot as plt                   # for most graphics
# from matplotlib.patches import ConnectionPatch    # for lines between subplots (used in the function "plot_line_accross_axes")


#####################    
# GENERAL FUNCTIONS #
#####################

def test_plot_line_accross_axes():
    # The function plot_line_accross_axes() draws a line in a figure object.
    #### At the moment I have no idea how to test this function
    assert 1 == 1

def test_plot_line_within_ax():
    # The function plot_line_within_ax() draws a line in a figure object.
    #### At the moment I have no idea how to test this function
    assert 1 == 1


def test_plot_endpoint():
    with pytest.raises(ValueError):
        plot_endpoint(ax=1, x=2, y=3, endpointcolor=dict())
    with pytest.raises(ValueError):
        plot_endpoint(ax=1, x=2, y=3, endpointcolor=[1,2,3])
    with pytest.raises(ValueError):
        plot_endpoint(ax=1, x=2, y=3, endpointcolor=[1,2], markersize_outercircle=5, markersize_innercircle=7)


#### Need to add more test-functions for automatic testing
