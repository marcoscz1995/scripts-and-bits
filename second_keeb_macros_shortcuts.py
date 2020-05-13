from math import radians, cos, sin, asin, sqrt
import numpy as np
import pandas as pd
from numpy import genfromtxt

df = pd.read_csv("geo_data_temp.csv")
df = df[['id', 'lat', 'long']]

#import the data as np arrays
df = df.to_numpy()
lat = df[:,1]
lon = df[:,2]
isd_cluster = np.zeros((45357,),dtype=int)
isd_cluster-=1
df = np.concatenate((df,isd_cluster[:,None]), axis=1)

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km


def geo_dist(df):
    reference_point = 0
    for i in list(range(reference_point,np.size(lat))):
        if df[reference_point,3]==-1:#has not been assigned a cluster yet
              iterator_list = list(range(reference_point,np.size(lat)))
              for j in iterator_list:
                  dist_to_reference = haversine(df[reference_point,2], df[reference_point,1], df[j,2], df[j,1])
                  if dist_to_reference<100:#less than 100km
                      df[j,3] = reference_point#else its left as -1
              reference_point = np.argmin(df[:,3]) #reference point becomes next zero value
              print(reference_point)
    return df

#import pdb; pdb.set_trace()
df = geo_dist(df)

#np.savetxt('struct_array.csv', df, delimiter=',', fmt=['%s' , '%f', '%f'], header='id,lat,lon', comments='')

