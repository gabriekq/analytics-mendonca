

import  pandas as pd
from  pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


def create_graph_per_area(save_path,year,graph_title):
    slice_data = [len(df_colunns[year & is_area_N]), len(df_colunns[year & is_area_S]),
                  len(df_colunns[year & is_area_W]), len(df_colunns[year & is_area_E])]
    plt.pie(slice_data, labels=crime_areas, startangle=60, shadow=True, explode=(0, 0.3, 0, 0), autopct='%1.1f%%')
    plt.title(graph_title)
    plt.legend()
    plt.savefig(save_path, bbox_inches='tight')
    plt.clf()

def create_graph_per_years(save_path,y_values):

   x_years = [x for x in range(2001,2019)]
   plt.plot(x_years,y_values)
   plt.savefig(save_path, bbox_inches='tight')




df = pd.read_csv('D:\Programacao\data\data_sets\Crimes_-_2001_to_present.csv')
image_path = "D:\\Programacao\\Python\\PyCharm-Projetos\\analytics-mendonca\\Resources\\images\\"
df_colunns = df.filter(items=['Date','Block']) # get the colunns that i want to use


df_colunns['Block'] = df_colunns['Block'].str.split(" ")
df_colunns['Block'] = df_colunns['Block'].str[1]

df_colunns['year'] = df_colunns['Date'].str.split(" ").str[0]
df_colunns['year'] = df_colunns['year'].str.split("/").str[2]

df_colunns['month'] = df_colunns['Date'].str.split(" ").str[0]
df_colunns['month'] = df_colunns['month'].str.split("/").str[1]

# only by year
#df_data_2001 = df_colunns[df_colunns['Date'] ==2001 ]
is_2001 = df_colunns['year'] == '2001'
is_2002 = df_colunns['year'] == '2002'
is_2003 = df_colunns['year'] == '2003'
is_2004 = df_colunns['year'] == '2004'
is_2005 = df_colunns['year'] == '2005'
is_2006 = df_colunns['year'] == '2006'
is_2007 = df_colunns['year'] == '2007'
is_2008 = df_colunns['year'] == '2008'
is_2009 = df_colunns['year'] == '2009'
is_2010 = df_colunns['year'] == '2010'
is_2011 = df_colunns['year'] == '2011'
is_2012 = df_colunns['year'] == '2012'
is_2013 = df_colunns['year'] == '2013'
is_2014 = df_colunns['year'] == '2014'
is_2015 = df_colunns['year'] == '2015'
is_2016 = df_colunns['year'] == '2016'
is_2017 = df_colunns['year'] == '2017'
is_2018 = df_colunns['year'] == '2018'
is_2019 = df_colunns['year'] == '2019'

is_area_N = df_colunns['Block'] == 'N'
is_area_S = df_colunns['Block'] == 'S'
is_area_W = df_colunns['Block'] == 'W'
is_area_E = df_colunns['Block'] == 'E'

# Crime Areas
crime_areas = ['North','South','West','East']

# Numbers of Crimes
total_crimes_2019_N = len(df_colunns[is_2019 & is_area_N])
total_crimes_2019_S = len(df_colunns[is_2019 & is_area_S])
total_crimes_2019_W = len(df_colunns[is_2019 & is_area_W])
total_crimes_2019_E = len(df_colunns[is_2019 & is_area_E])
total_crimes_2019 = len(df_colunns[is_2019])

total_crimes_2018_N = len(df_colunns[is_2018 & is_area_N])
total_crimes_2018_S = len(df_colunns[is_2018 & is_area_S])
total_crimes_2018_W = len(df_colunns[is_2018 & is_area_W])
total_crimes_2018_E = len(df_colunns[is_2018 & is_area_E])
total_crimes_2018 = len(df_colunns[is_2018])

total_crimes_2017_N = len(df_colunns[is_2017 & is_area_N])
total_crimes_2017_S = len(df_colunns[is_2017 & is_area_S])
total_crimes_2017_W = len(df_colunns[is_2017 & is_area_W])
total_crimes_2017_E = len(df_colunns[is_2017 & is_area_E])
total_crimes_2017 = len(df_colunns[is_2017])

total_crimes_2016_N = len(df_colunns[is_2016 & is_area_N])
total_crimes_2016_S = len(df_colunns[is_2016 & is_area_S])
total_crimes_2016_W = len(df_colunns[is_2016 & is_area_W])
total_crimes_2016_E = len(df_colunns[is_2016 & is_area_E])
total_crimes_2016 = len(df_colunns[is_2016])

total_crimes_2015_N = len(df_colunns[is_2015 & is_area_N])
total_crimes_2015_S = len(df_colunns[is_2015 & is_area_S])
total_crimes_2015_W = len(df_colunns[is_2015 & is_area_W])
total_crimes_2015_E = len(df_colunns[is_2015 & is_area_E])
total_crimes_2015 = len(df_colunns[is_2015])

total_crimes_2014_N = len(df_colunns[is_2014 & is_area_N])
total_crimes_2014_S = len(df_colunns[is_2014 & is_area_S])
total_crimes_2014_W = len(df_colunns[is_2014 & is_area_W])
total_crimes_2014_E = len(df_colunns[is_2014 & is_area_E])
total_crimes_2014 = len(df_colunns[is_2014])

total_crimes_2013_N = len(df_colunns[is_2013 & is_area_N])
total_crimes_2013_S = len(df_colunns[is_2013 & is_area_S])
total_crimes_2013_W = len(df_colunns[is_2013 & is_area_W])
total_crimes_2013_E = len(df_colunns[is_2013 & is_area_E])
total_crimes_2013 = len(df_colunns[is_2013])

total_crimes_2012_N = len(df_colunns[is_2012 & is_area_N])
total_crimes_2012_S = len(df_colunns[is_2012 & is_area_S])
total_crimes_2012_W = len(df_colunns[is_2012 & is_area_W])
total_crimes_2012_E = len(df_colunns[is_2012 & is_area_E])
total_crimes_2012 = len(df_colunns[is_2012])

total_crimes_2011_N = len(df_colunns[is_2011 & is_area_N])
total_crimes_2011_S = len(df_colunns[is_2011 & is_area_S])
total_crimes_2011_W = len(df_colunns[is_2011 & is_area_W])
total_crimes_2011_E = len(df_colunns[is_2011 & is_area_E])
total_crimes_2011 = len(df_colunns[is_2011])

total_crimes_2010_N = len(df_colunns[is_2010 & is_area_N])
total_crimes_2010_S = len(df_colunns[is_2010 & is_area_S])
total_crimes_2010_W = len(df_colunns[is_2010 & is_area_W])
total_crimes_2010_E = len(df_colunns[is_2010 & is_area_E])
total_crimes_2010 = len(df_colunns[is_2010])

total_crimes_2009_N = len(df_colunns[is_2009 & is_area_N])
total_crimes_2009_S = len(df_colunns[is_2009 & is_area_S])
total_crimes_2009_W = len(df_colunns[is_2009 & is_area_W])
total_crimes_2009_E = len(df_colunns[is_2009 & is_area_E])
total_crimes_2009 = len(df_colunns[is_2009])

total_crimes_2008_N = len(df_colunns[is_2008 & is_area_N])
total_crimes_2008_S = len(df_colunns[is_2008 & is_area_S])
total_crimes_2008_W = len(df_colunns[is_2008 & is_area_W])
total_crimes_2008_E = len(df_colunns[is_2008 & is_area_E])
total_crimes_2008 = len(df_colunns[is_2008])

total_crimes_2007_N = len(df_colunns[is_2007 & is_area_N])
total_crimes_2007_S = len(df_colunns[is_2007 & is_area_S])
total_crimes_2007_W = len(df_colunns[is_2007 & is_area_W])
total_crimes_2007_E = len(df_colunns[is_2007 & is_area_E])
total_crimes_2007 = len(df_colunns[is_2007])

total_crimes_2006_N = len(df_colunns[is_2006 & is_area_N])
total_crimes_2006_S = len(df_colunns[is_2006 & is_area_S])
total_crimes_2006_W = len(df_colunns[is_2006 & is_area_W])
total_crimes_2006_E = len(df_colunns[is_2006 & is_area_E])
total_crimes_2006 = len(df_colunns[is_2006])

total_crimes_2005_N = len(df_colunns[is_2005 & is_area_N])
total_crimes_2005_S = len(df_colunns[is_2005 & is_area_S])
total_crimes_2005_W = len(df_colunns[is_2005 & is_area_W])
total_crimes_2005_E = len(df_colunns[is_2005 & is_area_E])
total_crimes_2005 = len(df_colunns[is_2005])

total_crimes_2004_N = len(df_colunns[is_2004 & is_area_N])
total_crimes_2004_S = len(df_colunns[is_2004 & is_area_S])
total_crimes_2004_W = len(df_colunns[is_2004 & is_area_W])
total_crimes_2004_E = len(df_colunns[is_2004 & is_area_E])
total_crimes_2004 = len(df_colunns[is_2004])

total_crimes_2003_N = len(df_colunns[is_2003 & is_area_N])
total_crimes_2003_S = len(df_colunns[is_2003 & is_area_S])
total_crimes_2003_W = len(df_colunns[is_2003 & is_area_W])
total_crimes_2003_E = len(df_colunns[is_2003 & is_area_E])
total_crimes_2003 = len(df_colunns[is_2003])

total_crimes_2002_N = len(df_colunns[is_2002 & is_area_N])
total_crimes_2002_S = len(df_colunns[is_2002 & is_area_S])
total_crimes_2002_W = len(df_colunns[is_2002 & is_area_W])
total_crimes_2002_E = len(df_colunns[is_2002 & is_area_E])
total_crimes_2002 = len(df_colunns[is_2002])

total_crimes_2001_N = len(df_colunns[is_2001 & is_area_N])
total_crimes_2001_S = len(df_colunns[is_2001 & is_area_S])
total_crimes_2001_W = len(df_colunns[is_2001 & is_area_W])
total_crimes_2001_E = len(df_colunns[is_2001 & is_area_E])
total_crimes_2001 = len(df_colunns[is_2001])

#Graphs
create_graph_per_area(save_path=image_path+'Chicago-2019.png',year=is_2019,graph_title="Chicago Crimes at 2019")
create_graph_per_area(save_path=image_path+'Chicago-2018.png',year=is_2018,graph_title="Chicago Crimes at 2018")
create_graph_per_area(save_path=image_path+'Chicago-2017.png',year=is_2017,graph_title="Chicago Crimes at 2017")
create_graph_per_area(save_path=image_path+'Chicago-2016.png',year=is_2016,graph_title="Chicago Crimes at 2016")
create_graph_per_area(save_path=image_path+'Chicago-2015.png',year=is_2015,graph_title="Chicago Crimes at 2015")
create_graph_per_area(save_path=image_path+'Chicago-2014.png',year=is_2014,graph_title="Chicago Crimes at 2014")
create_graph_per_area(save_path=image_path+'Chicago-2013.png',year=is_2013,graph_title="Chicago Crimes at 2013")
create_graph_per_area(save_path=image_path+'Chicago-2012.png',year=is_2012,graph_title="Chicago Crimes at 2012")
create_graph_per_area(save_path=image_path+'Chicago-2011.png',year=is_2011,graph_title="Chicago Crimes at 2011")
create_graph_per_area(save_path=image_path+'Chicago-2010.png',year=is_2010,graph_title="Chicago Crimes at 2010")
create_graph_per_area(save_path=image_path+'Chicago-2009.png',year=is_2009,graph_title="Chicago Crimes at 2009")
create_graph_per_area(save_path=image_path+'Chicago-2008.png',year=is_2008,graph_title="Chicago Crimes at 2008")
create_graph_per_area(save_path=image_path+'Chicago-2007.png',year=is_2007,graph_title="Chicago Crimes at 2007")
create_graph_per_area(save_path=image_path+'Chicago-2006.png',year=is_2006,graph_title="Chicago Crimes at 2006")
create_graph_per_area(save_path=image_path+'Chicago-2005.png',year=is_2005,graph_title="Chicago Crimes at 2005")
create_graph_per_area(save_path=image_path+'Chicago-2004.png',year=is_2004,graph_title="Chicago Crimes at 2004")
create_graph_per_area(save_path=image_path+'Chicago-2003.png',year=is_2003,graph_title="Chicago Crimes at 2003")
create_graph_per_area(save_path=image_path+'Chicago-2002.png',year=is_2002,graph_title="Chicago Crimes at 2002")
create_graph_per_area(save_path=image_path+'Chicago-2001.png',year=is_2001,graph_title="Chicago Crimes at 2001")

x = [total_crimes_2001,total_crimes_2002,total_crimes_2003,total_crimes_2004,total_crimes_2005,total_crimes_2006,total_crimes_2007,total_crimes_2008,total_crimes_2009,
     total_crimes_2010,total_crimes_2011,total_crimes_2012,total_crimes_2013,total_crimes_2014,total_crimes_2015,total_crimes_2016,total_crimes_2017,total_crimes_2018]

#create_graph_per_years(save_path=image_path+'Chicago-total-crimes.png',y_values=x)

#df_unique_date = DataFrame(df_colunns["Date"])
#df_unique_date = df_unique_date.sort_values(by='Date').drop_duplicates('Date')
#print(df_unique_date.head(n=20))


print("total of crimes at 2001: ",total_crimes_2001)
print("total of crimes at 2002: ",total_crimes_2002)
print("total of crimes at 2003: ",total_crimes_2003)
print("total of crimes at 2004: ",total_crimes_2004)
print("total of crimes at 2005: ",total_crimes_2005)
print("total of crimes at 2006: ",total_crimes_2006)
print("total of crimes at 2007: ",total_crimes_2007)
print("total of crimes at 2008: ",total_crimes_2008)
print("total of crimes at 2009: ",total_crimes_2009)
print("total of crimes at 2010: ",total_crimes_2010)
print("total of crimes at 2011: ",total_crimes_2011)
print("total of crimes at 2012: ",total_crimes_2012)
print("total of crimes at 2013: ",total_crimes_2013)
print("total of crimes at 2014: ",total_crimes_2014)
print("total of crimes at 2015: ",total_crimes_2015)
print("total of crimes at 2016: ",total_crimes_2016)
print("total of crimes at 2017: ",total_crimes_2017)
print("total of crimes at 2018: ",total_crimes_2018)
print("total of crimes at 2019: ",total_crimes_2019)
