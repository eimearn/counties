"""
Title: Programming for GIS Assignment 1
Author: Eimear Nicholl
Programme purpose: The purpose of this programme is to read and perform tasks on the CSO 'counties' dataset
Specific tasks
1. Download and save the counties dataset as a shapefile. You can get this at
http://mf2.dit.ie:8080/geoserver/cso/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=cso:ctygeom&outputFormat=SHAPE-ZIP
2. Merge the Dublin local authorities into one and store in a new shapefile. Don't forget to store the attributes as
 well as the geometry.
3. Calculate the centroid for Dublin merged and store this in a new shapefile.
4. Geocode the address of this centroid. You will need to convert the CRS to WGS84. This should be stored in the
shapefile you created in the last step.
Suggestions
- Store downloaded files like ctygeom in their own directory/folder in your PyCharm project. Give this a sensible
name such as "counties" in this example. By using this scheme you can download it once and use it in different programs.
- Store files created such as the merged shapefile and centroid in a separate directory/folder. Name this something like
 ".cache". The leading "." indicates a hidden directory/folder. This is designed to be sacrificial. You can delete its contents without losing anything of value.
- There is an error in the Geopy library so for the geocoding part of the exercise, download and use geopy_corrected.py
 from my GitHub page. Import this into your program.

"""
import requests
import zipfile
import io


#import file from online

url = 'http://mf2.dit.ie:8080/geoserver/cso/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=cso:ctygeom&outputFormat=SHAPE-ZIP'

print('Downloading shapefile...')
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
print("Done")
# z.extractall(path='tmp/') # extract to folder
filenames = [y for y in sorted(z.namelist()) for ending in ['dbf', 'prj', 'shp', 'shx'] if y.endswith(ending)]
print(filenames)