#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""NetCDF"""

import netCDF4
import numpy as np


def load_dataset(nc_file):
    '''Load nc-file into dataset'''
    return netCDF4.Dataset(nc_file, mode='r')

def print_metadata(filehandle):
    '''Print metadata'''
    # Metadata
    print(f'Metadata: {filehandle}')

    # Dictionaries
    print(f'Dictionaries: {filehandle.__dict__}')

def print_dimensions(filehandle):
    '''Print dimensions'''
    for dim in filehandle.dimensions.values():
        print(f'Dimension: {dim}')
    print(f'Dimensions: {filehandle.dimensions}')


def print_variables(filehandle):
    '''Print variables'''
    for var in filehandle.variables.values():
        print(f'Variable: {var}')
    print(f'Variables: {filehandle.variables.keys()}')


def get_coords(filehandle):
    '''Get coords'''
    #lons = fh.variables['lon'][80:100, 85:100]
    #lats = fh.variables['lat'][65:100, 90:100]
    lons = filehandle.variables['lon'][:]
    lats = filehandle.variables['lat'][:]
    return lons, lats

def get_values(filehandle, variable='prediction'):
    '''Get values from variable'''
    return filehandle.variables[variable][:]



def get_closest(lats,lons,lat_pt,lon_pt):

  dist_2 = (lats-lat_pt)**2 + (lons-lon_pt)**2
  min_dist = dist_2.argmin()

  return np.unravel_index(min_dist, lats.shape)



def main():
    ''' Test '''
    data = load_dataset('INTER_OPER_R___RD1NRT__L3__20140204T080000_20140205T080000_0001.nc')

    print('                                                     ')
    print('=====================================================')


    print_metadata(data)

    #print_dimensions(data)

    #print_variables(data)

    #print(get_coords(data))

    # Print all values
    #for variable in data.variables.keys():
    #    print(f'Variable: {variable}')
    #    #print(f'    type: {type(get_values(data,variable))}')
    #    print(f'    values: {get_values(data,variable).compressed()}')
    #prediction = data.variables['prediction']
    #print(prediction)

    #lons = data.variables['lon'][:]
    #lats = data.variables['lat'][:]
    #print(f'Lon: {lons.mean()}, lat: {lats.mean()}')
    #y_min,x_min = get_closest(lats, lons, 60,24)
    #print(y_min, x_min)


    data.close()

if __name__ == "__main__":
    main()
