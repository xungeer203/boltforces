# Summary
Place loads in the center of a pattern, of bolts for example.  
Calculate Fax, Fshv and Fshw forces for each bolt.

# Details
Fax = axial force of an bolt  
Fshv = shear force in v-direction of an bolt  
Fshw = shear force in w-direction of an bolt  
v, w = v-, w-position of an bolt  
v0, w0 = center of the pattern  
Fu, Fv, Fw, Mu, Mv, Mw = external load in the center of pattern  
load_list = [Fu, Fv, Fw, Mu, Mv, Mw]

# input
each bolt's position: v_list, w_list  
load in the center of pattern: load_list
# output
a .csv file

# to do
plot the pattern with matplotlib  
read input from .csv file
