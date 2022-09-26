# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:04:37 2021

@author: Darshan Rathod
"""


import matplotlib as _mpl
import matplotlib.pyplot as _plt
import numpy as _np
import pandas as _pd
import os as _os

from . import shared as _shared


def make_dir(path1):
    try:
        _os.mkdir(path1)
    except FileExistsError as e:
        pass


def get_dir_path(fname):
    return [_os.path.join(fname,x) for x in _os.listdir(fname) if _os.path.isdir(_os.path.join(fname,x))]

def get_file_path(fname):
    return [_os.path.join(fname,x) for x in _os.listdir(fname) if _os.path.isfile(_os.path.join(fname,x))]

def get_dir_name(fname):
    return [x for x in _os.listdir(fname) if _os.path.isdir(_os.path.join(fname,x))]

def get_file_name(fname):
    return [x for x in _os.listdir(fname) if _os.path.isfile(_os.path.join(fname,x))]



def move_origin(d1,xnew=0, ynew=0):
    d1['x'] = d1['x'] - xnew
    d1['y'] = d1['y'] - ynew
    return d1

def rotate_coordinates_degrees(x,y,angle=0):
    xy1 = _np.array([x.flatten(),y.flatten()])
    cos1 = _np.cos(angle*_np.pi/180)
    sin1 = _np.sin(angle*_np.pi/180)
    Rv = _np.array([[cos1,-sin1],[sin1,cos1]])
    xy1 = _np.matmul(Rv,xy1)
    x = xy1[0,:].reshape(x.shape)
    y = xy1[1,:].reshape(y.shape)
    return x,y

def rotate_bases(d1,angle=0):
    mask1 = d1['u'].mask
    uv = _np.array([d1['u'].data.flatten(),d1['v'].data.flatten()])
    theta1 = angle * _np.pi/180
    A = _np.array([[_np.cos(theta1),_np.sin(theta1)],[-_np.sin(theta1),_np.cos(theta1)]]).T
    Ainv = _np.linalg.inv(A)
    uv1 = _np.matmul(Ainv,uv)
    d1['u'] = uv1[0,:].reshape(d1['u'].shape)
    d1['u'] = _np.ma.masked_array(d1['u'],mask=mask1,fill_value=0,dtype='float64')
    d1['v'] = uv1[1,:].reshape(d1['v'].shape)
    d1['v'] = _np.ma.masked_array(d1['v'],mask=mask1,fill_value=0,dtype='float64')
    return d1


def imshow(img,*args,**kwargs):
    _plt.imshow(img,*args,**kwargs)
    _plt.xticks([])
    _plt.yticks([])


def decode_A1(case_name):
    str1 = case_name.upper()
    idx1 = str1.index('_A_')
    astr1 = ''
    g = 0
    for i in range(idx1+2,len(str1),1):
        if str1[i].isdigit():
            g = 1
            astr1 = astr1 + str1[i]
        elif g == 1:
            break
    return int(astr1)

def decode_s1(case_name):
    str1 = case_name.upper()
    idx1 = str1.index('_S_')
    astr1 = ''
    g = 0
    for i in range(idx1+2,len(str1),1):
        if str1[i].isdigit():
            g = 1
            astr1 = astr1 + str1[i]
        elif g == 1:
            break
    return int(astr1)


def decode_holes1(proj_name):
    str1 = proj_name.lower()
    try:
        idx1 = str1.index('holes')
        str2 = str1[idx1:idx1+12]
        if 'close' in str2:
            return 'close'
        elif 'open' in str2:
            return 'open'
    except ValueError as e:
        return 'open'


def get_exp_props(filepath,air=None,seeding=None,pressure=None,trial=None):
    data1 = _pd.read_excel(filepath)    
    if air is not None:
        f1 = data1['m_air'] == air
        data1 = data1[f1]
    if seeding is not None:
        f1 = data1['m_seeding'] == seeding
        data1 = data1[f1]
    if pressure is not None:
        f1 = data1['P_inlet'] == pressure
        data1 = data1[f1]
    if trial is not None:
        f1 = data1['trial'] == trial
        data1 = data1[f1]
    return data1















