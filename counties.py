"""
Title: Programming for GIS Assignment 1
Author: Eimear Nicholl
Date: 25/03/2019
Programme purpose: The purpose of this programme is to read and perform tasks on the CSO 'counties' dataset
Specific tasks
1. Download and save the counties dataset as a shapefile. You can get this at
http://mf2.dit.ie:8080/geoserver/cso/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=cso:ctygeom&outputFormat=SHAPE-ZIP
2.. Merge the Dublin local authorities into one and store in a new shapefile. Don't forget to store the attributes as
 well as the geometry.
3. Calculate the centroid for Dublin merged and store this in a new shapefile.
4. Geocode the address of this centroid. You will need to convert the CRS to WGS84. This should be stored in the
shapefile you created in the last step.

"""

import requests
import zipfile
import fiona
import shapely
import pyproj


#import and saving file
#code adapted from code by Lauren Oldja at https://medium.com/@loldja/reading-shapefile-zips-from-a-url-in-python-3-93ea8d727856
#import file from online

url = 'http://mf2.dit.ie:8080/geoserver/cso/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=cso:ctygeom&outputFormat=SHAPE-ZIP'
path = input("Enter a shapefile name in the format of path/to/") #https://github.com/markfoleyie/gisp2019/blob/master/fiona_read_1.py

def download_shp(url): #function created to download and save shp file from url
    print('Downloading shapefile...')
    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    print("Done")
    z.extractall(path)
    # extract to folder of the path provided by the user in 'path'
    filenames = [y for y in sorted(z.namelist()) for ending in ['dbf', 'prj', 'shp', 'shx'] if y.endswith(ending)]
    print(filenames)
    return

download_shp(url) #run download_shp function


#2 Merge the Dublin local authorities into one and store in a new shapefile.

#function to find local aouthorities into one shp file and merge the counties into one polygon

shp= (path)/ctygeom.shp

def merge(shp):                         # this function will merge all the county polygons in Dublin.
    if __name__ == "__main__":
        shp = "ctygeom.shp"
        features = []
        with fiona.Env():
            with fiona.open(shp, "r") as fh:
                for feature in fh:
                    if "ingal" in feature["properties"]["countyname"]: #first for loop finds all dublin counties under 'countyname'
                        features.append(feature)
                    elif "ublin_city" in feature["properties"]["countyname"]:
                        features.append(feature)
                    elif "outh_dublin" in feature["properties"]["countyname"]:
                        features.append(feature)
                    elif "dunlaoghaire–rathdown" in feature["properties"]["countyname"]:
                        features.append(feature)
                    else:
                        print("does no compute")
        result = geom_info(features[0], features[1]) #all counties are put in features list
        print("g1 Info\n" + "-" * 20)       #the list is then accessed with a for loop and the cascade_union method is applied to merge.
        for k in result[0].items():
            k = shapely.cascade_union(result)
    return


merge(shp)

#now save as new shp
#structure from https://gis.stackexchange.com/questions/266526/union-intersected-polygons-with-python-and-save-the-result-in-a-new-shapefile

driver = ogr.GetDriverByName('ESRI Shapefile')
try:
    ds_out = driver.CreateDataSource("dub_merge.shp")     #saves the file as an shp
except:
    raise Exception("File already exists.")

# Grab current layer's SRS and geometry type.
srs = layer_in.GetSpatialRef()
geom_type = layer_in.GetGeomType()

# Create empty layer.
layer_out = ds_out.CreateLayer(name = "dublin", srs = 2157, geom_type = polygon)

# Copy fields
layer_defn = results.GetLayerDefn()
n_fields = layer_defn.GetFieldCount()
for i in range(n_fields):
    layer_out.CreateField(layer_defn.GetFieldDefn(i))

#3 Find centroid of merged Dublin File

dub_centroid = dublin.centroid.wkt

#3 save dublin centroid as new shp

driver = ogr.GetDriverByName('dub_centroid')
try:
    ds_out = driver.CreateDataSource("centroid.shp")
except:
    raise Exception("File already exists.")

srs = layer_in.GetSpatialRef()
geom_type = layer_in.GetGeomType()

layer_out = ds_out.CreateLayer(name = dub_centroid, srs = 2157, geom_type = polygon)

# Copy fields
layer_defn = dub_centroid.GetLayerDefn()
n_fields = layer_defn.GetFieldCount()
for i in range(n_fields):
    layer_out.CreateField(layer_defn.GetFieldDefn(i))

dub_centroid.save(path)

#4

def transform_coordinates(souce_crs, target_crs, source_coord_pair):   #from masters github/pyprojtransformation.py
    proj = []                                                           #transforms dublin centroid into wgs84
    try:
        for crs in (souce_crs, target_crs, source_coord_pair ):
            if type(crs) == str:
                crs_split = crs.split(":")
                if crs_split[0].lower() == "epsg":
                    proj.append(pyproj.Proj(init=crs))
                else:
                    proj.append(pyproj.Proj(crs))
            elif type(crs) == dict and "proj" in crs:
                crs = to_string(crs)
                proj.append(pyproj.Proj(crs))
            else:
                raise ValueError("CRS must be string or dictionary")

        return pyproj.transform(proj[0], proj[1], source_coord_pair[0], source_coord_pair[1])

    except ValueError as e:
        print("ERROR: {}".format(e))
        quit(3)
    except Exception as e:
        print("ERROR: {}".format(e))
        quit(4)

transform_coordinates(29902, 4326, dub_centroid)
dub_centroid.save(path)











