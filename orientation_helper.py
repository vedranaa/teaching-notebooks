"""
Plotly and matplotlib helper functions for orientation analysis.

Author: vand@dtu.dk
"""

import plotly.graph_objects as go
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import numpy as np
import scmap
from icosphere import icosphere


def show_vol_orientation(V, vec, z, coloring, alpha=0.5, ax=None):

    dim = V.shape[1:]
    vectors = vec[:,z].reshape(3, -1).T
    rgb = coloring(vectors).reshape(dim + (3,))
    rgba = np.concatenate((rgb, alpha * np.ones(dim + (1,))), axis=2)
    if ax is None:
        fig, ax = plt.subplots()
    ax.imshow(V[z], cmap=plt.cm.gray)
    ax.imshow(rgba)
    ax.set_title(f'slice z={z}')


def show_vol_flow(V, vec, z, s=5, double_arrow = False, ax=None):   
      
    xmesh, ymesh = np.mgrid[0:V.shape[1], 0:V.shape[2]]
    if ax is None:
      fig, ax = plt.subplots()
    ax.imshow(V[z], cmap=plt.cm.gray)
    g = slice(s//2, None, s)
    ax.quiver(ymesh[g, g], xmesh[g, g], vec[0, z, g, g], vec[1, z, g, g],
              color='r', angles='xy')
    if double_arrow:
        ax.quiver(ymesh[g, g], xmesh[g, g], -vec[0, z, g, g], -vec[1, z, g, g],
              color='r', angles='xy')
    ax.set_title(f'slice z={z}')

def show_coloring_sphere_matplotlib(coloring, nu=15):

    vertices, faces = icosphere(nu)
    face_vectors = vertices[faces].sum(axis=1)
    face_vectors /= np.sqrt((face_vectors**2).sum(axis=1, keepdims=True))

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')                  

    face_colors = coloring(face_vectors)

    poly = mpl_toolkits.mplot3d.art3d.Poly3DCollection(vertices[faces])
    poly.set_facecolor(face_colors) 
    poly.set_edgecolor(None)
    poly.set_linewidth(0.25)

    ax.add_collection3d(poly)
        
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)

    ax.azim = 40
    ax.dist = 10
    ax.elev = 35

    ax.set_xticks([-1,0,1])
    ax.set_yticks([-1,0,1])
    ax.set_zticks([-1,0,1])
        
    plt.show()

# Plotly helper functions

def show_scatter_points(vec, coloring, random_subset=1000):
    
    random_sample = np.random.choice(vec.size//3, size=random_subset, replace=False)
    xyz = vec.reshape((3, -1))[:, random_sample]  # random sample of direction vectors
    xyz = np.hstack([xyz, -xyz])  # add antipodal points

    rgb = coloring(xyz.T)
    scatter = [go.Scatter3d(x=xyz[0], y=xyz[1], z=xyz[2], mode='markers', marker=dict(color=rgb))]
    unit = {'range': [-1, 1], 'autorange': False}
    scene = {'xaxis': unit, 'yaxis': unit, 'zaxis': unit, 'aspectratio': {'x': 1, 'y':1, 'z':1 }}
    layout = {'width': 600, 'height': 600, 'scene': scene}

    fig = go.Figure(data=scatter, layout=layout)
    fig.show()


def show_coloring_sphere(coloring, nu=15):

    vertices, faces = icosphere(nu)
    vertex_colors = coloring(vertices)

    gm = go.Mesh3d(x=vertices[:,0], y=vertices[:,1], z=vertices[:,2], 
            i=faces[:,0], j=faces[:,1], k=faces[:,2], 
            vertexcolor = vertex_colors, showlegend=False)
    
    unit = {'range': [-1, 1], 'autorange': False}
    scene = {'xaxis': unit, 'yaxis': unit, 'zaxis': unit, 'aspectratio': {'x': 1, 'y':1, 'z':1 }}
    layout = {'width': 600, 'height': 600, 'scene': scene}

    fig = go.Figure(data=gm, layout=layout)
    fig.show()
