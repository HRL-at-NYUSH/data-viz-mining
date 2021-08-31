first = '''
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
data = pd.read_csv("'''
second = '''.csv")
data["New"] =  data["Coordinates"].progress_apply(get_loc)
df = pd.DataFrame(data)
df.to_csv("'''
third = '''_geo_out.csv")'''

init = 0
while init<=11871:#871:
    with open('proc_'+str(init)+'.py','w',encoding='utf-8') as f:
        f.write(first+str(init)+second+str(init)+third)
    init = init+1
import pandas as pd
g = pd.read_csv('geocoded_census_for_all_year.csv')
i = 0
start = 0
while i<=11871:#871:
    p = g[start:start+1000]
    p.to_csv(str(i)+'.csv')
    start = start+1000
    i+=1
