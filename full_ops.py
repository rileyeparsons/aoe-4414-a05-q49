# full_ops.py

# Usage: python3 full_ops.py c_in n_wv

# Parameters:
#  c_in : int 
#   input channel count
#  n_wv : int 
#   number of weight vectors

# Output:
#  c_out : list
#  output channel count
#  h_out : list
#  output height count
#  w_out : list
#  output width count
#  adds : list
#  number of additions performed
#  muls : list
#  number of multiplications performed
#  divs : list
#  number of divisions performed

# Written by Riley Parsons

import sys
import math

# "constants"
w = 7.292115e-5

# helper functions  
def output_map_h(h_in, p, h_pool, s):
  h_out = ((h_in + 2*p - h_pool)/s) +  1
  return h_out

def output_map_w(w_in, p, w_pool, s):
  w_out = ((w_in + 2*p - w_pool)/s) +  1
  return w_out

def get_muls(n_wv, c_in):
  muls = n_wv*c_in
  return muls

def get_adds(n_wv, c_in):
  adds = n_wv*c_in
  return adds

def get_divs(c_in, h_out, w_out):
  divs = c_in*h_out*w_out
  return divs

# main function
def full_ops(c_in, n_wv):
  
  c_out = n_wv
  h_out = 1
  w_out = 1
  muls = get_muls(n_wv, c_in)
  adds = get_adds(n_wv, c_in)
  divs = 0

  print(c_out)
  print(h_out)
  print(w_out)
  print(adds)
  print(muls)
  print(divs)

  return muls, adds
  
# initialize script arguments
c_out = None
n_wv = None

# parse script arguments
if len(sys.argv)==3:
    c_in = int(sys.argv[1])
    n_wv = int(sys.argv[2])
else:
  print('Usage: python3 full_ops.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km')
  exit()

# write script below this line
if __name__ == '__main__':
  full_ops(c_in, n_wv)
else:
  full_ops(c_in, n_wv)