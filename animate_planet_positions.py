from __future__ import unicode_literals
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math

import make_planets
import planet_angle

def plot_circle(r):

    x = []
    y = []

    for i in range(360):
        x.append(r*math.cos(math.radians(i)))
        y.append(r*math.sin(math.radians(i)))

    plt.plot(x, y, color='k')
    return

def setup_solar_sys(planet_list):

    mpl.rcParams['savefig.dpi'] = 500
    #mpl.rcParams['fontsize'] = 14
    mpl.rc('font', family='Arial')
    fig = plt.figure(figsize=(10,10))

    #plot sun
    plt.scatter([0], [0], marker='o', color='goldenrod', s=1000)
  

    for planet in planet_list:

        plot_circle(planet.plot_radius)

    plt.axis('equal')
    plt.axis('off')

    return fig

year=1993
month=7
day=19
hour=22
minute=30
seccond=0

#Get the planets 
planet_list = make_planets.make_planets()
fig = setup_solar_sys(planet_list)

#Get the angle of each planet given the date
for planet in planet_list:
    planet = planet_angle.planet_angle(planet, year, month, day, hour, minute, seccond)

for planet in planet_list:
    planet.x_position = planet.plot_radius*math.cos(math.radians(planet.angle))
    planet.y_position = planet.plot_radius*math.sin(math.radians(planet.angle))
    plt.text(planet.x_position, planet.y_position, planet.symbol, zorder=200)

plt.scatter([planet.x_position for planet in planet_list], [planet.y_position for planet in planet_list], c=[planet.colour for planet in planet_list], s=400, zorder=100)


plt.savefig('planet_position.png')


