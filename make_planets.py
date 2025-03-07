from __future__ import unicode_literals

class planet(object):

    name = ''
    symbol = ''
    colour = ''
    radius = 0.
    plot_radius = 0.
    x_position = 0.
    y_position = 0.
    angle = 0


def make_planets():

    mercury = planet()
    mercury.name = 'Mercury'
    mercury.symbol = '☿'
    mercury.radius = 0.387
    mercury.plot_radius = 3
    mercury.colour = 'orange'
    mercury.x_position = mercury.radius
    mercury.y_position = 0.
    mercury.angle = 0

    venus = planet()
    venus.name = 'Venus'
    venus.symbol = '♀'
    venus.radius = 0.723
    venus.plot_radius = 4
    venus.colour = 'goldenrod'
    venus.x_position = venus.radius
    venus.y_position = 0.
    venus.angle = 0
 
    earth = planet()
    earth.name = 'Earth'
    earth.symbol = '♁'
    earth.radius = 1
    earth.plot_radius = 5
    earth.colour = 'DodgerBlue'
    earth.x_position = earth.radius
    earth.y_position = 0.
    earth.angle = 0

    mars = planet()
    mars.name = 'Mars'
    mars.symbol = '♂'
    mars.radius = 1.524
    mars.plot_radius = 6
    mars.colour = 'salmon'
    mars.x_position = mars.radius
    mars.y_position = 0.
    mars.angle = 0

    jupiter = planet()
    jupiter.name = 'Jupiter'
    jupiter.symbol = '♃'
    jupiter.radius = 5.203
    jupiter.plot_radius = 8
    jupiter.colour = 'bisque'
    jupiter.x_position = jupiter.radius
    jupiter.y_position = 0.
    jupiter.angle = 0

    saturn = planet()
    saturn.name = 'Saturn'
    saturn.symbol = '♄'
    saturn.radius = 9.539
    saturn.plot_radius = 10.5
    saturn.colour = 'gold'
    saturn.x_position = saturn.radius
    saturn.y_position = 0.
    saturn.angle = 0

    uranus = planet()
    uranus.name = 'Uranus'
    uranus.symbol = '♅'
    uranus.radius = 19.18
    uranus.plot_radius = 13
    uranus.colour = 'CadetBlue'
    uranus.x_position = uranus.radius
    uranus.y_position = 0.
    uranus.angle = 0

    neptune = planet()
    neptune.name = 'Neptune'
    neptune.symbol = '♆'
    neptune.radius = 30.06
    neptune.plot_radius = 15.5
    neptune.colour = 'SlateBlue'
    neptune.x_position = neptune.radius
    neptune.y_position = 0.
    neptune.angle = 0

    '''
    pluto = planet()
    pluto.name = 'Pluto'
    pluto.radius = 39.53
    pluto.plot_radius = 18
    pluto.colour = 'gray'
    pluto.x_position = pluto.radius
    pluto.y_position = 0.
    pluto.angle = 0
    '''

    planet_list = [mercury, venus, earth, mars, jupiter, saturn, neptune, uranus]
    return planet_list
