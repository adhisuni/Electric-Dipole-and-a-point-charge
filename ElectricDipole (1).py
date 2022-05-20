#!/usr/bin/env python
# coding: utf-8

# In[1]:


from vpython import *

# Definition of important constants  
kcoulomb = 9e9  #  Coulomb’s constant 
qproton = 1.6e-19 # charge of a proton in Coulomb
E_scale = 4e-22
print("The charge of a proton is", qproton, "Coulombs")

# Definition of the charges  

# Defining a positive charge as a sphere, with its positon vector, radius, color and gving it the charge of a proton
plus = sphere(pos = vector(-2e-10, 0, 0), radius = 1e-11, color = color.red, q = qproton) 

# Defining a negative charge as a sphere, with its positon vector, radius, color and gving it the negative charge of a proton
minus = sphere(pos = vector(+2e-10,0,0), radius = 1e-11, color = vector(0,0,1), q = -qproton)

# Defining a proton as a sphere, with its positon vector, radius, charge, proton mass ‘m’ (given in kg), 
# the proton momentum ‘p’, and a trail to follow the motion of the proton from step to step.
proton = sphere(pos = vector(5e-10, 3e-10, 4e-10), radius = 1e-11, color = color.cyan,
                q = 1.6e-19, m = 1.7e-27, p = vector(0,0,0), trail = curve(color = color.white))



# Defining a dipole, which is a list of the plus and minus charge
dipole = [plus, minus]

# Definition of the grid of points at which to calculate the field
locations = [] # this will store different locations, at which we are interested in finding the field
dx = 1e-10 # this is our step size, that we use to get different coordinates along the x axis
dy = 1e-10 # this is our step size, that we use to get different coordinates along the y axis
dz = 1e-10 # this is our step size, that we use to get different coordinates along the z axis



# looping over all the different x coordinates
for x in arange(-4.5e-10, 4.5e-10 + dx, dx):
    # for each x coordinate, looping over all the possible y coordinates
    for y in arange(-4.5e-10, 4.5e-10 + dy, dy):
        # # for each y coordinate, looping over all the possible z coordinates
        for z in arange(-4.5e-10, 4.5e-10 + dz, dz):
            # creating a vector with the x,y and z coordinates
            a = vector(x, y, z)
            # appending the vector 'a' to to the 'locations' list
            locations.append(a) 
            
            
            

# Routine to calculate the electric field
#E = vector(0, 0, 0) # initializing the electric field variable ‘E’ as a vector of zero length

# relative position vector 𝑟 between the charge and the location at which we want to find 𝐸.
#r = plus.pos - locations
#print("The relative position vector is", r)

# finding the magnitude 'rmag' of our 'r' vector, the formula 
#rmag = sqrt((r.x ** 2) + (r.y ** 2) + (r.z ** 2))
#print("The magnitude of the relative position vector is", rmag)

# finding the unit vector 'rhat' by dividing 'r' by its magnitude 'rmag'
#rhat = r/rmag
#print("The unit vector of the relative position vector is", rhat)


# Defining a arrow ‘pos_arrow’, the position attribute for this arrow is the vector locating the arrow’s
# tail and the axis is the vector providing the arrow’s orientation. 
# In the output we will see a white arrow representing the relative position vector show up when we run your program. 
# pos_arrow = arrow(pos = plus.pos, axis = r, color = color.white, shaftwidth = 1e-11)

# calculating the value of the electric field variable ‘E’ at the location of interest due to the positive charge
# we have used the electric field formula that includes the coulomb's constant, the magnitude of r vector and the unit vector
#E = E + ((kcoulomb * plus.q/(rmag**2)) * rhat) 
#print("The value of the electric field due to the positive charge is", E)

# Defined ‘E_arrow’ to visualize  the electric field, the tail located at the vector given by ‘locations’ 
# and an orientation in the direction of ‘E’. The quantity ‘E_scale’ is an arbitrary scale factor to make the
# arrow comparable in size to the two spheres (otherwise the length of the arrow would be enormous
# because the value of ‘E’ is much larger as a number than the radius of the spheres). 
# we have used E_scale to scale the electric field arrow
# E_arrow = arrow(pos = locations, axis = E_scale * E, color = color.yellow)


# This code calculates the electric field for each charge in our dipole
# Routine to calculate the electric field
#E = vector(0, 0, 0)
#for charge in dipole:
#    r = charge.pos - locations
#    rmag = sqrt((r.x ** 2) + (r.y ** 2) + (r.z ** 2))
#    rhat = r/rmag
#    E = E + ((kcoulomb * charge.q/(rmag**2)) * rhat)


# E_arrow = arrow(pos = locations, axis = E_scale * E, color = color.yellow)




# this code calculates the electric field for each point in our locations and for each charge in our dipole
# looping over each point vector in our locations list
for point in locations:
    # defining Electric Field as a zero vector
    E = vector(0, 0, 0)
    # looping over each charge in our dipole
    for charge in dipole:
        # these are the same steps for calculating the electric field that we did earlier, 
        # the only difference is that they are now inside a for loop and will be repeated
        # many times for each point in our locations and for each charge in our dipole
        r = charge.pos - point
        rmag = sqrt((r.x ** 2) + (r.y ** 2) + (r.z ** 2)) 
        rhat = r/rmag
        E = E + ((kcoulomb * charge.q/(rmag**2)) * rhat)
    #  visualizing the electric field at each point
    E_arrow = arrow(pos = point, axis = E_scale * E, color = color.yellow)
    
    
    

# Simulate the trajectory of a proton
dt = 1e-17 # this is our increment value i.e. with every iteration of our while loop with increase the time by 1e-17
t=0 # this is the start time

while t < 3e-13:
    rate(1000) # ‘rate()’ command updates the display window
    t = t + dt
    E = vector(0,0,0)
    for charge in dipole:
        r = proton.pos - charge.pos
        E = E + kcoulomb * charge.q * norm(r) / mag(r)**2
        F = proton.q * E
        proton.p = proton.p + F * dt
        proton.pos = proton.pos + (proton.p / proton.m) * dt
        # ‘proton.trail.append()’ command appends the latest step to the overall trail tracking the proton’s trajectory
        proton.trail.append(proton.pos)


# In[ ]:





# In[ ]:





# In[ ]:




