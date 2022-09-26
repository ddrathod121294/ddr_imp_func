# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 21:04:55 2022

@author: darsh
"""

import matplotlib as _mpl
import matplotlib.pyplot as _plt
import numpy as _np
import pandas as _pd


def remove_ax_lines(ax):
    for spine in ['top', 'right','bottom','left']:
        ax.spines[spine].set_visible(False)
    return ax

# def plot_quiver(vel_set=None,n=0,data=None,ax=None,fracx=6,fracy=None,scale=0.8,width=0.1,headwidth=12,headlength=15,minshaft=2,minlength=0.1,units='xy',scale_units='xy'):
def plot_quiver(vel_set=None,n=0,data=None,ax=None,fracx=6,fracy=None,**kwargs):
    if ax is None:
        ax = _plt.gca()
    
    if data is None:
        data = vel_set.make_quiver_data(n=n,fracx=fracx,fracy=fracy)
    else:
        if fracy is None:
            fracy = fracx
        x= data['x']
        y = data['y']
        u = data['u']
        v = data['v']
        idx = []
        for i in range(0,x.shape[0],fracy):
            idx.append(i)
        x1 = x[idx]
        y1 = y[idx]
        u1 = u[idx]
        v1 = v[idx]
        
        for i in range(0,x1.shape[1],fracx):
            idx.append(i)
        x1 = x1[:,idx]
        y1 = y1[:,idx]
        u1 = u1[:,idx]
        v1 = v1[:,idx]
        
        data = {'x': x1, 'y':y1,
                'u': u1, 'v':v1}
    
    # ax.quiver(data['x'],data['y'],data['u'],data['v'],
    #            # linewidths = width,
    #           width=width,
    #           headwidth=headwidth,
    #           headlength=headlength,
    #           minshaft=minshaft,minlength=minlength,
    #           units=units,scale_units=scale_units,scale=scale)
    
    
    ax.quiver(data['x'],data['y'],data['u'],data['v'],**kwargs)
    
    return ax
    
def plot_colorbar(ax=None,cax=None,vmax='max',vmin='min',colormap='jet',
                  ctitle='',font_size=25,cticks=11,roundto=2):
    if vmax == 'max':
        vmax = 1
    if vmin == 'min':
        vmin = 0
    
    cmap = _plt.get_cmap(colormap,256)
    norm = _mpl.colors.Normalize(vmin=vmin,vmax=vmax)
    sm = _plt.cm.ScalarMappable(cmap=cmap,norm=norm)
    
    if cax is None:
        if ax is None:
            ax = _plt.gca()
        cbar = _plt.colorbar(sm,ax=ax,ticks = _np.linspace(vmin*0.99,vmax,cticks,endpoint=True).round(roundto),orientation='vertical')
    else:
        cbar = _plt.colorbar(sm,cax=cax,ticks = _np.linspace(vmin*0.99,vmax,cticks,endpoint=True).round(roundto),orientation='vertical')
        
    cbar.ax.set_title(ctitle,fontsize=font_size,pad=25)
    cbar.ax.tick_params(labelsize=font_size)
    return ax


def plot_contourf(vel_set=None,n=0,data=None,z='u',ax=None,vmax='max',vmin='min',
                  add_colorbar=True,colormap='jet',ctitle='',font_size=25,cticks=10,levels=200,alpha=1,
                  roundto=2):
    
    if ax is None:
        ax = _plt.gca()
    if data is None:
        data = vel_set.make_contour_data(n=n,z=z)
    if vmax == 'max':
        vmax = _np.quantile(data['z'].data,0.99)
    if vmin == 'min':
        vmin = _np.quantile(data['z'].data,0.01)
    
    cmap = _plt.get_cmap(colormap,256)
    norm = _mpl.colors.Normalize(vmin=vmin,vmax=vmax)
    
    cp = ax.contourf(data['x'],data['y'],data['z'],
                     levels=levels,cmap=cmap,norm=norm,corner_mask=True,alpha=alpha)
    
    if add_colorbar:
        plot_colorbar(ax=ax,vmax=vmax,vmin=vmin,colormap=colormap,ctitle=ctitle,
                     font_size=font_size,cticks=cticks,roundto=roundto)
    
    return ax


def plot_image(vel_set=None,n=0,frame=0,data=None,ax=None,vmin=0,vmax=3000,levels=20,colormap='viridis',alpha=1):
    
    if ax is None:
        ax = _plt.gca()
    
    if data is None:
        data = vel_set.make_image_data(n=n,frame=frame)
    
    cmap = _plt.get_cmap(colormap,256)
    norm = _mpl.colors.Normalize(vmin=vmin,vmax=vmax)
    
    cp = ax.contourf(data['x'],data['y'],data['z'],levels=levels,corner_mask=True,
                     cmap=cmap,norm=norm,alpha=alpha)
    return ax


def plot_streamlines(vel_set=None,n=0,data=None,ax=None,density=(5,5),linewidth=1,color='white'):
    
    if ax is None:
        ax = _plt.gca()
    
    if data is None:
        data = vel_set.make_streamline_data(n=n)
    
    ax.streamplot(data['x'],data['y'],data['u'][::-1],data['v'][::-1],
                  density=density,linewidth=linewidth,color=color)
    
    return ax



