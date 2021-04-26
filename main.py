from pathlib import Path
import xarray as xr
import netCDF4
import glob
import holoviews as hv
from holoviews import opts
hv.extension('matplotlib')

NC_PATH = 'data/'
SAVE_PATH = 'plot/'

def main():
    nc_list = get_nc()
    basemap = build_basemap(nc_list)
    hv.save(basemap, 'basemap.png', path=SAVE_PATH)


def get_nc():
    nc_list = glob.glob(NC_PATH + '/*.nc')
    return nc_list


def build_basemap(nc_list):
    ds_platform = xr.open_mfdataset(nc_list, group='Platform', concat_dim='location_time', combine='by_coords').to_dataframe()
    pathing_plot = hv.Scatter(ds_platform, vdims='longitude', kdims='latitude')
    return pathing_plot

if __name__ == '__main__':
    main()