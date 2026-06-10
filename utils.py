import matplotlib.pyplot as plt

def plot_ebm_vs_esm(time_ebm, temp_ebm, time_esm, temp_esm, temp_control=None):
    
    fig = plt.figure(figsize=(10,5))
    
    if temp_control is not None:
        plt.plot(time_esm, temp_control, lw=0.8, label='piControl', c='grey')

    plt.plot(time_esm, temp_esm, lw=0.8, label='ESM', c='k')
    plt.plot(time_ebm, temp_ebm, label='EBM')

    # Fig settings
    plt.grid(alpha=0.3)
    plt.legend()
    plt.xlabel('time')
    plt.ylabel('global mean temperature [°C]')