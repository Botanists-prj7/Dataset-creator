from gridmaker import *

crs_earth = 'EPSG:4326'
crs_maps = 'EPSG:3857'
crs = crs_maps

gridsizes = [100000] #100km grid size
update_csv_files = False #Set true if CSV files should be updated
plot_grid = True
using_mac = False

for gridsize in gridsizes:
    soiltypeColumnName = 'soiltype'
    centerColumnName = 'center'

    if using_mac: 
        dk_soiltype_geodataframe = convert_shp_to_gdf_using_crs('data\\Jordart_200000_Shape\\jordart_200000.shp',crs)
        dk_geodataframe_grid = convert_gdf_to_gdfgrid(dk_soiltype_geodataframe,gridsize,crs) 
    else:
        dk_soiltype_geodataframe = convert_shp_to_gdf_using_crs('data/Jordart_200000_Shape/Jordart_200000.shp',crs)
        dk_geodataframe_grid = convert_gdf_to_gdfgrid(dk_soiltype_geodataframe,gridsize) 

    #Adding relevant data to our geodataframe
    dk_geodataframe_grid[soiltypeColumnName] = ''
    dk_geodataframe_grid[centerColumnName] = dk_geodataframe_grid.centroid

    #Going through all grids an finding the needed soiltype
    bar = Bar('Finding soiltype of all gridcells', max=len(dk_geodataframe_grid.index))
    output_dk_grid = []
    for index, grid in dk_geodataframe_grid.iterrows():    
        found_soiltype = get_soiltype_of_point(dk_soiltype_geodataframe,grid[centerColumnName]) 
        if not (found_soiltype is None):
            output_dk_grid.append([grid['geometry'], found_soiltype])        
        else :
            corner_soiltype = find_soiltype_of_cornerpoints(dk_soiltype_geodataframe,grid['geometry'])
            if not (corner_soiltype is None):
                output_dk_grid.append([grid['geometry'], corner_soiltype])        
        bar.next()
    bar.finish()    

    output_dk_gdf_grid = gpd.GeoDataFrame(output_dk_grid, columns=['geometry', soiltypeColumnName])

    if(plot_grid):
        output_dk_gdf_grid.plot(column = soiltypeColumnName) 
        plt.show()

    if(update_csv_files):
        save_gdf_to_csv_in_folder('csv_files',f'DK_Soiltypes_{gridsize}.csv',output_dk_gdf_grid)
        output_dk_gdf_grid.drop(soiltypeColumnName, inplace=True, axis=1)
        save_gdf_to_csv_in_folder('csv_files',f'DK_Grid_{gridsize}.csv',output_dk_gdf_grid)