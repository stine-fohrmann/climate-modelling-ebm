import xarray as xr
import numpy as np

def get_global_mean():
    # Open dataset
    # TODO define filepaths to data in separate file
    ds_pi =xr.open_dataset('../data/tas_Amon_MPI-ESM1-2-LR_piControl_r1i1p1f1_g025_185001-284912.nc') 
    ds1  = xr.open_dataset('../data/tas_Amon_MPI-ESM1-2-LR_historical-ssp245_r25i1p1f1_g025_185001-210012.nc')
    ds2  = xr.open_dataset('../data/tas_Amon_MPI-ESM1-2-LR_historical-ssp245_r1i1p1f1_g025_185001-210012.nc')

    # Compute weights for weighing by area (so poles aren't overrepresented)
    weights = np.cos(np.deg2rad(ds1.lat))

    # Compute global mean temp
    global_mean1   = ds1.tas.weighted(weights).mean(dim=['lat', 'lon']).resample(time='YS').mean()
    global_mean2   = ds2.tas.weighted(weights).mean(dim=['lat', 'lon']).resample(time='YS').mean()
    global_mean_pi = ds_pi.tas.weighted(weights).mean(dim=['lat', 'lon']).resample(time='YS').mean().sel(time=slice('1850-01-01', '2100-01-01'))

    return global_mean1, global_mean2, global_mean_pi