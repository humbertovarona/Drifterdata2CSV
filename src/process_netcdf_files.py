def process_netcdf_files(input_directory, output_file):
    nc_files = glob.glob(os.path.join(input_directory, '*.nc'))

    with open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Drifter_ID', 'Start_date', 'Final_date'])

        for nc_file in nc_files:
            drifter_id, start_date, final_date = get_netcdf_attributes(nc_file)
            csv_writer.writerow([drifter_id, start_date, final_date])
