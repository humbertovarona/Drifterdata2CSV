def get_netcdf_attributes(file):
    with Dataset(file, 'r') as nc_file:
        drifter_id = nc_file.getncattr('Drifter_ID')
        start_date = nc_file.getncattr('Start_date')
        final_date = nc_file.getncattr('Final_date')
    return drifter_id, start_date, final_date
