#%%
import urllib.request, json

#%% read data
x = "http://maps.googleapis.com/maps/api/geocode/json?address=google";

with urllib.request.urlopen(x) as url:
    data = json.loads(url.read().decode())
    

print(data)