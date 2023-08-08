import pandas as pd

def split_coordinates(dframe):
    lat_list = []
    long_list = []
    for i in range(len(dframe)):
        coords = eval(dframe.loc[i, "coordinates"])
        lat_list.append(coords["latitude"])
        long_list.append(coords["longitude"])
    dframe["latitude"] = lat_list
    dframe["longitude"] = long_list

def split_datetime(dframe):
    utc_list = []
    local_list = []
    for i in range(len(dframe)):
        dtime = eval(dframe.loc[i, "date"])
        utc_list.append(dtime["utc"])
        local_list.append(dtime["local"])
    dframe["utc"] = utc_list
    dframe["local"] = local_list

wokalna = pd.read_csv("wokalna.csv")
wokalna["city"] = "Warszawa"

split_coordinates(wokalna)
split_datetime(wokalna)
wokalna["utc"] = pd.to_datetime(wokalna["utc"])
wokalna["local"] = pd.to_datetime(wokalna["local"])

#drop unnecessary columns
cols=["isMobile", "isAnalysis", "entity", "sensorType", "date", "coordinates"]
wokalna.drop(columns=cols, inplace=True, axis=1)

wokalna.to_csv("wokalna_clean.csv")