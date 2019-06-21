import  pandas as pd
from numpy.distutils.system_info import xft_info
from  pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np



def create_graph_Years(df_colunns,image_path):
    is_monday = 0
    is_tuesday = 0
    is_wednesday = 0
    is_thursday = 0
    is_friday = 0
    is_saturday = 0
    is_sunday = 0

    for rowId , day in df_colunns['Day'].iteritems():

        if(day == 'Monday'):
           is_monday = is_monday + 1
        elif(day == 'Tuesday'):
            is_tuesday = is_tuesday + 1
        elif( day =='Wednesday'):
            is_wednesday = is_wednesday + 1
        elif(day == 'Thursday'):
            is_thursday = is_thursday+ 1
        elif(day == 'Friday'):
            is_friday = is_friday +1
        elif(day == 'Saturday'):
            is_saturday = is_saturday +1
        elif(day == 'Sunday'):
            is_sunday = is_sunday +1

    x = np.arange(7)
    crimes = np.array([is_monday,is_tuesday,is_wednesday,is_thursday,is_friday,is_saturday,is_sunday])
    plt.figure(figsize=(15, 10))
    plt.bar(x,crimes,align = "center", alpha = 0.5)
    plt.xticks(x,('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'))

    xmin = np.amin(crimes) - 3000
    xmax = np.amax(crimes) + 3000
   # plt.xticks(np.arange(xmin, xmax, 2.0))
    plt.ylim( ymin=xmin,ymax=xmax)

    plt.savefig(image_path,bbox_inches='tight')
    plt.clf()


df = pd.read_csv('Q:\Programacao\data\data_sets\Crimes_-_2001_to_present.csv')
image_path = 'Q:\\Programacao\\Python\\PyCharm-Projetos\\analytics-mendonca\\src\Resources\\images\\'
df_colunns = df.filter(items=['Date','Block']) # get the colunns that i want to use

df_colunns['Block'] = df_colunns['Block'].str.split(" ")
df_colunns['Block'] = df_colunns['Block'].str[1]

df_colunns['year'] = df_colunns['Date'].str.split(" ").str[0]
df_colunns['year'] = df_colunns['year'].str.split("/").str[2]    #indice 3 ano

df_colunns['month'] = df_colunns['Date'].str.split(" ").str[0]
df_colunns['month'] = df_colunns['month'].str.split("/").str[0]  #indice 1 mes

df_colunns['Date'] = df_colunns['Date'].str.split(" ").str[0]


df_colunns['Date'] = pd.to_datetime(df_colunns['Date'], format="%m/%d/%Y")
df_colunns['Day'] = df_colunns['Date'].dt.day_name()


is_january = df_colunns['month'] == '01'
is_february = df_colunns['month'] == '02'
is_march = df_colunns['month'] == '03'
is_april = df_colunns['month'] == '04'
is_may = df_colunns['month'] == '05'
is_june = df_colunns['month'] == '06'
is_july = df_colunns['month'] == '07'
is_august = df_colunns['month'] == '08'
is_september = df_colunns['month'] == '09'
is_october = df_colunns['month'] == '10'
is_november = df_colunns['month'] == '11'
is_december = df_colunns['month'] == '12'

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
days_week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


#terminar em transformar de contar dias da semana em variaeis
#print(df_colunns.head(n=5))
#print(df_colunns[is_2001])

##for rowId , day in df_colunns['Day'].iteritems():

create_graph_Years(df_colunns[is_2001],image_path=image_path+"weekend-Crimes-2001.png")
create_graph_Years(df_colunns[is_2002],image_path=image_path+"weekend-Crimes-2002.png")
create_graph_Years(df_colunns[is_2003],image_path=image_path+"weekend-Crimes-2003.png")
create_graph_Years(df_colunns[is_2004],image_path=image_path+"weekend-Crimes-2004.png")
create_graph_Years(df_colunns[is_2005],image_path=image_path+"weekend-Crimes-2005.png")
create_graph_Years(df_colunns[is_2006],image_path=image_path+"weekend-Crimes-2006.png")
create_graph_Years(df_colunns[is_2007],image_path=image_path+"weekend-Crimes-2007.png")
create_graph_Years(df_colunns[is_2008],image_path=image_path+"weekend-Crimes-2008.png")
create_graph_Years(df_colunns[is_2009],image_path=image_path+"weekend-Crimes-2009.png")
create_graph_Years(df_colunns[is_2010],image_path=image_path+"weekend-Crimes-2010.png")
create_graph_Years(df_colunns[is_2011],image_path=image_path+"weekend-Crimes-2011.png")
create_graph_Years(df_colunns[is_2012],image_path=image_path+"weekend-Crimes-2012.png")
create_graph_Years(df_colunns[is_2013],image_path=image_path+"weekend-Crimes-2013.png")
create_graph_Years(df_colunns[is_2014],image_path=image_path+"weekend-Crimes-2014.png")
create_graph_Years(df_colunns[is_2015],image_path=image_path+"weekend-Crimes-2015.png")
create_graph_Years(df_colunns[is_2016],image_path=image_path+"weekend-Crimes-2016.png")
create_graph_Years(df_colunns[is_2017],image_path=image_path+"weekend-Crimes-2017.png")
create_graph_Years(df_colunns[is_2018],image_path=image_path+"weekend-Crimes-2018.png")
create_graph_Years(df_colunns[is_2019],image_path=image_path+"weekend-Crimes-2019.png")
create_graph_Years(df_colunns,image_path=image_path+"weekend-Crimes-Total.png")

#create_graph_year(df_colunns[is_2001])

