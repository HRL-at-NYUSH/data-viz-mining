
import shapely
from shapely.geometry import Point # Point class
from shapely.geometry import shape # shape() is a function to convert geo objects through the interface
import geopandas as gpd
from tqdm import tqdm
#from pandarallel import pandarallel
# Initialization
#pandarallel.initialize()
#pandarallel.initialize()
tqdm.pandas()
fp = "geo_export_1d615ae4-45a8-4466-8a86-d25e49ffb305.shp"
datas = gpd.read_file(fp)
p = (-73.9984,40.7195) # an x,y tuple
def get_loc(p):
    p = str(p)
    try:
        palpha = p.replace('(','').replace(')','').split(',')[1]
        pbeta = p.replace('(','').replace(')','').split(',')[0]
        p = (float(palpha),float(pbeta))
        i = 0
        
        g = []
        while i<=len(datas)-1:
            if (Point(p).within(shape(datas.loc[i]['geometry'])))==True:
                return (datas.loc[i]['ntaname'])
                break
          #  g.append(data.loc[i]['ntaname'])
            i+=1
    except:
        return None
import pandas as pd
data = pd.read_csv("0.csv")
data["New"] =  data["Coordinates"].progress_apply(get_loc)
df = pd.DataFrame(data)
df.to_csv("0_geo_out.csv")