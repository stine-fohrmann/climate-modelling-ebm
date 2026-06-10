import math

# Universal constants
pi = math.pi

# Time
ORIGINAL_dt      = 86400.0                              # seconds in 24 h
secday  = 86400.0                              # seconds in 24 h
secyear = 86400.0 * 360.0                      # seconds in 1 yr
ORIGINAL_maxtime = 20.0 * secyear              # max time in seconds

# Effective emissivity [1]
ORIGINAL_eps = 0.61

# Stefan-Boltzmann constant [W/m²/K⁴]
ORIGINAL_sigma = 5.67e-8 

# Planetary albedo [1]
ORIGINAL_alpha = 0.3

# Annual average of solar constant [W/m²]
ORIGINAL_solar = 1370.0

# Mixed layer depth: depth of the fluid column [m]
ORIGINAL_H = 70.0

# Density of fluid [kg/m³]
ORIGINAL_rho = 1025

# Specific heat of fluid [J/kg/K]
ORIGINAL_cp = 4000.0

# Heat capacity [J/K/m²]
ORIGINAL_ce = ORIGINAL_cp*ORIGINAL_rho*ORIGINAL_H

# Initial global mean surface temperature [K]
ORIGINAL_T_ini = 285.15