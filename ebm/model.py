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

    ce = cp*ORIGINAL_rho*H


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

def run_with_changing_H_and_albedo(
    T_ini   =ORIGINAL_T_ini, 
    solar   =ORIGINAL_solar,
    alpha_init=ORIGINAL_alpha,
    d_alpha=0,
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
    alpha = np.zeros(itmax)

    T_abs[0] = T_ini

    alpha[0] = alpha_init


    # time loop
    for it in range(0, itmax-1):

        # Compute incoming SW radiation
        shortwave = 0.25 * solar * (1-alpha[it])

        # Update albedo
        alpha[it+1] = alpha[it] + d_alpha*alpha[it]

        # Compute outgoing LW radiation
        longwave  = eps * sigma * T_abs[it]**4

        # Compute absolute temperature
        T_abs[it+1] = T_abs[it] + dt * (shortwave - longwave)/ce

        dH = 0.001 * T_abs[it]
        # H = H + dH

        ce = cp*rho*H

        # advance time
        time[it+1] = time[it] + dt

    # Convert T_abs to Celcius
    T = T_abs - 273.15

    # Convert time axis to years
    time = time/(secday*360)

    return T, time, alpha

# def H_from_temperature(T_abs_prev, H_min, H_max, T_ref, slope):
#     """Mixed layer depth depends on temperature"""
#     # print(T_abs_prev-273.15)
#     H = (T_abs_prev-273.15)+50
#     # print(H)
#     # H = -1.7*(T_abs_prev-273.15)+50
#     # H = T_abs_prev*slope
#     return H
#     # return np.clip(H, H_min, H_max)

# def model_mld(T_ini   =ORIGINAL_T_ini, 
#     solar   =ORIGINAL_solar,
#     alpha   =ORIGINAL_alpha, 
#     eps     =ORIGINAL_eps, 
#     sigma   =ORIGINAL_sigma, 
#     H_init       =ORIGINAL_H, 
#     maxtime =ORIGINAL_maxtime, 
#     dt      =ORIGINAL_dt, 
#     ce      =ORIGINAL_ce, 
#     cp      =ORIGINAL_cp
#     ):

#     itmax = int(maxtime/dt)

#     # Initialization
#     time  = np.zeros(itmax)
#     T_abs = np.zeros(itmax)
#     H = np.zeros(itmax)

#     T_abs[0] = T_ini
#     H[0]     = H_init

#     for it in range(0, itmax-1):
#         shortwave = 0.25 * solar * (1-alpha)
#         longwave  = eps * sigma * T_abs[it]**4
        
#         # Update temperature
#         T_abs[it+1] = T_abs[it] + dt * (shortwave - longwave)/ce
        
#         # advance time
#         time[it+1] = time[it] + dt

#         rho = ORIGINAL_rho
#         cp = ORIGINAL_cp
#         # Update H based on current temperature
#         H[it+1] = H_from_temperature(T_abs[it], H_min=50, H_max=70, T_ref=T_ini, slope=0.02)
#         ce      = cp * rho * H[it+1]


#     # Convert T_abs to Celcius
#     T = T_abs - 273.15

#     # Convert time axis to years
#     time = time/(secday*360)

#     return T, time, H


def albedo_of_time(t, alpha_init, slope):
    alpha = alpha_init + slope*t

    return alpha

def model_alpha(params):
    T_ini = params['T_init'] if params.get('T_init') else ORIGINAL_T_ini
    solar = ORIGINAL_solar
    ce    = params['ce'] if params.get('ce') else ORIGINAL_ce
    sigma = params['sigma'] if params.get('sigma') else ORIGINAL_sigma
    eps   = params['eps'] if params.get('eps') else ORIGINAL_eps
    H     = params['H'] if params.get('H') else ORIGINAL_H
    cp    = params['cp'] if params.get('cp') else ORIGINAL_cp
    alpha_init  = params['alpha_init'] if params.get('alpha_init') else ORIGINAL_alpha
    alpha_slope = params['alpha_slope'] # slope per sec
    
    maxtime = params['maxtime'] if params.get('maxtime') else ORIGINAL_maxtime
    dt = params['dt'] if params.get('dt') else ORIGINAL_dt

    itmax = int(maxtime/dt)

    # Initialization
    time  = np.zeros(itmax)
    T_abs = np.zeros(itmax)
    alpha = np.zeros(itmax)

    for i in range(len(T_abs)):
        T_abs[i] = T_ini

    for i in range(len(alpha)):
        alpha[i] = alpha_init

    ce = cp*ORIGINAL_rho*H

    # time loop
    for it in range(0, itmax-1):

        # Compute planetary albedo
        alpha[it+1] = albedo_of_time(t=it*dt, alpha_init=alpha_init, slope=alpha_slope)

        # Compute incoming SW radiation
        shortwave = 0.25 * solar * (1-alpha[it])

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

    return T, time, alpha