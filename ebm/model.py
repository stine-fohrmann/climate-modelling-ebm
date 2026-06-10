import numpy as np
from ebm.params import *

def run_model(
    T_ini   =ORIGINAL_T_ini, 
    solar   =ORIGINAL_solar,
    alpha   =ORIGINAL_alpha, 
    eps     =ORIGINAL_eps, 
    sigma   =ORIGINAL_sigma, 
    H       =ORIGINAL_H, 
    maxtime =ORIGINAL_maxtime, 
    dt      =ORIGINAL_dt, 
    ce      =ORIGINAL_ce, 
    cp      =ORIGINAL_cp
    ):

    itmax = int(maxtime/dt)

    # Initialization
    time  = np.zeros(itmax)
    T_abs = np.zeros(itmax)

    T_abs[0] = T_ini

    # time loop
    for it in range(0, itmax-1):

        # Compute incoming SW radiation
        shortwave = 0.25 * solar * (1-alpha)

        # Compute outgoing LW radiation
        longwave  = eps * sigma * T_abs[it]**4

        # Compute absolute temperature
        T_abs[it+1] = T_abs[it] + dt * (shortwave - longwave)/ce

        # advance time
        time[it+1] = time[it] + dt

    # Convert T_abs to Celcius
    T = T_abs - 273.15

    # Convert time axis to years
    time = time/(secday*360)

    return T, time


def run_with_changing_H(
    T_ini   =ORIGINAL_T_ini, 
    solar   =ORIGINAL_solar,
    alpha   =ORIGINAL_alpha, 
    eps     =ORIGINAL_eps, 
    sigma   =ORIGINAL_sigma, 
    H       =ORIGINAL_H, 
    maxtime =ORIGINAL_maxtime, 
    dt      =ORIGINAL_dt, 
    ce      =ORIGINAL_ce, 
    cp      =ORIGINAL_cp,
    rho=ORIGINAL_rho
    ):

    itmax = int(maxtime/dt)

    # Initialization
    time  = np.zeros(itmax)
    T_abs = np.zeros(itmax)

    T_abs[0] = T_ini

    # time loop
    for it in range(0, itmax-1):

        # Compute incoming SW radiation
        shortwave = 0.25 * solar * (1-alpha)

        # Compute outgoing LW radiation
        longwave  = eps * sigma * T_abs[it]**4

        # Compute absolute temperature
        T_abs[it+1] = T_abs[it] + dt * (shortwave - longwave)/ce

        dH = 0.001 * T_abs[it]
        H = H + dH

        ce = cp*rho*H

        # advance time
        time[it+1] = time[it] + dt

    # Convert T_abs to Celcius
    T = T_abs - 273.15

    # Convert time axis to years
    time = time/(secday*360)

    return T, time