import  pandas as pd
from  pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np





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


# Terminar fazer a junsao de mes com ano

crimes_2001_january = len(df_colunns[is_2001 & is_january])
crimes_2001_february = len(df_colunns[is_2001 & is_february])
crimes_2001_march = len(df_colunns[is_2001 & is_march])
crimes_2001_april = len(df_colunns[is_2001 & is_april])
crimes_2001_may = len(df_colunns[is_2001 & is_may])
crimes_2001_june = len(df_colunns[is_2001 & is_june])
crimes_2001_july = len(df_colunns[is_2001 & is_july])
crimes_2001_august = len(df_colunns[is_2001 & is_august])
crimes_2001_september = len(df_colunns[is_2001 & is_september])
crimes_2001_october = len(df_colunns[is_2001 & is_october])
crimes_2001_november = len(df_colunns[is_2001 & is_november])
crimes_2001_december = len(df_colunns[is_2001 & is_december])


crimes_2002_january = len(df_colunns[is_2002 & is_january])
crimes_2002_february = len(df_colunns[is_2002 & is_february])
crimes_2002_march = len(df_colunns[is_2002 & is_march])
crimes_2002_april = len(df_colunns[is_2002 & is_april])
crimes_2002_may = len(df_colunns[is_2002 & is_may])
crimes_2002_june = len(df_colunns[is_2002 & is_june])
crimes_2002_july = len(df_colunns[is_2002 & is_july])
crimes_2002_august = len(df_colunns[is_2002 & is_august])
crimes_2002_september = len(df_colunns[is_2002 & is_september])
crimes_2002_october = len(df_colunns[is_2002 & is_october])
crimes_2002_november = len(df_colunns[is_2002 & is_november])
crimes_2002_december = len(df_colunns[is_2002 & is_december])


crimes_2003_january = len(df_colunns[is_2003 & is_january])
crimes_2003_february = len(df_colunns[is_2003 & is_february])
crimes_2003_march = len(df_colunns[is_2003 & is_march])
crimes_2003_april = len(df_colunns[is_2003 & is_april])
crimes_2003_may = len(df_colunns[is_2003 & is_may])
crimes_2003_june = len(df_colunns[is_2003 & is_june])
crimes_2003_july = len(df_colunns[is_2003 & is_july])
crimes_2003_august = len(df_colunns[is_2003 & is_august])
crimes_2003_september = len(df_colunns[is_2003 & is_september])
crimes_2003_october = len(df_colunns[is_2003 & is_october])
crimes_2003_november = len(df_colunns[is_2003 & is_november])
crimes_2003_december = len(df_colunns[is_2003 & is_december])


crimes_2004_january = len(df_colunns[is_2004 & is_january])
crimes_2004_february = len(df_colunns[is_2004 & is_february])
crimes_2004_march = len(df_colunns[is_2004 & is_march])
crimes_2004_april = len(df_colunns[is_2004 & is_april])
crimes_2004_may = len(df_colunns[is_2004 & is_may])
crimes_2004_june = len(df_colunns[is_2004 & is_june])
crimes_2004_july = len(df_colunns[is_2004 & is_july])
crimes_2004_august = len(df_colunns[is_2004 & is_august])
crimes_2004_september = len(df_colunns[is_2004 & is_september])
crimes_2004_october = len(df_colunns[is_2004 & is_october])
crimes_2004_november = len(df_colunns[is_2004 & is_november])
crimes_2004_december = len(df_colunns[is_2004 & is_december])

crimes_2005_january = len(df_colunns[is_2005 & is_january])
crimes_2005_february = len(df_colunns[is_2005 & is_february])
crimes_2005_march = len(df_colunns[is_2005 & is_march])
crimes_2005_april = len(df_colunns[is_2005 & is_april])
crimes_2005_may = len(df_colunns[is_2005 & is_may])
crimes_2005_june = len(df_colunns[is_2005 & is_june])
crimes_2005_july = len(df_colunns[is_2005 & is_july])
crimes_2005_august = len(df_colunns[is_2005 & is_august])
crimes_2005_september = len(df_colunns[is_2005 & is_september])
crimes_2005_october = len(df_colunns[is_2005 & is_october])
crimes_2005_november = len(df_colunns[is_2005 & is_november])
crimes_2005_december = len(df_colunns[is_2005 & is_december])

crimes_2006_january = len(df_colunns[is_2006 & is_january])
crimes_2006_february = len(df_colunns[is_2006 & is_february])
crimes_2006_march = len(df_colunns[is_2006 & is_march])
crimes_2006_april = len(df_colunns[is_2006 & is_april])
crimes_2006_may = len(df_colunns[is_2006 & is_may])
crimes_2006_june = len(df_colunns[is_2006 & is_june])
crimes_2006_july = len(df_colunns[is_2006 & is_july])
crimes_2006_august = len(df_colunns[is_2006 & is_august])
crimes_2006_september = len(df_colunns[is_2006 & is_september])
crimes_2006_october = len(df_colunns[is_2006 & is_october])
crimes_2006_november = len(df_colunns[is_2006 & is_november])
crimes_2006_december = len(df_colunns[is_2006 & is_december])


crimes_2007_january = len(df_colunns[is_2007 & is_january])
crimes_2007_february = len(df_colunns[is_2007 & is_february])
crimes_2007_march = len(df_colunns[is_2007 & is_march])
crimes_2007_april = len(df_colunns[is_2007 & is_april])
crimes_2007_may = len(df_colunns[is_2007 & is_may])
crimes_2007_june = len(df_colunns[is_2007 & is_june])
crimes_2007_july = len(df_colunns[is_2007 & is_july])
crimes_2007_august = len(df_colunns[is_2007 & is_august])
crimes_2007_september = len(df_colunns[is_2007 & is_september])
crimes_2007_october = len(df_colunns[is_2007 & is_october])
crimes_2007_november = len(df_colunns[is_2007 & is_november])
crimes_2007_december = len(df_colunns[is_2007 & is_december])

crimes_2008_january = len(df_colunns[is_2008 & is_january])
crimes_2008_february = len(df_colunns[is_2008 & is_february])
crimes_2008_march = len(df_colunns[is_2008 & is_march])
crimes_2008_april = len(df_colunns[is_2008 & is_april])
crimes_2008_may = len(df_colunns[is_2008 & is_may])
crimes_2008_june = len(df_colunns[is_2008 & is_june])
crimes_2008_july = len(df_colunns[is_2008 & is_july])
crimes_2008_august = len(df_colunns[is_2008 & is_august])
crimes_2008_september = len(df_colunns[is_2008 & is_september])
crimes_2008_october = len(df_colunns[is_2008 & is_october])
crimes_2008_november = len(df_colunns[is_2008 & is_november])
crimes_2008_december = len(df_colunns[is_2008 & is_december])

crimes_2009_january = len(df_colunns[is_2009 & is_january])
crimes_2009_february = len(df_colunns[is_2009 & is_february])
crimes_2009_march = len(df_colunns[is_2009 & is_march])
crimes_2009_april = len(df_colunns[is_2009 & is_april])
crimes_2009_may = len(df_colunns[is_2009 & is_may])
crimes_2009_june = len(df_colunns[is_2009 & is_june])
crimes_2009_july = len(df_colunns[is_2009 & is_july])
crimes_2009_august = len(df_colunns[is_2009 & is_august])
crimes_2009_september = len(df_colunns[is_2009 & is_september])
crimes_2009_october = len(df_colunns[is_2009 & is_october])
crimes_2009_november = len(df_colunns[is_2009 & is_november])
crimes_2009_december = len(df_colunns[is_2009 & is_december])

crimes_2010_january = len(df_colunns[is_2010 & is_january])
crimes_2010_february = len(df_colunns[is_2010 & is_february])
crimes_2010_march = len(df_colunns[is_2010 & is_march])
crimes_2010_april = len(df_colunns[is_2010 & is_april])
crimes_2010_may = len(df_colunns[is_2010 & is_may])
crimes_2010_june = len(df_colunns[is_2010 & is_june])
crimes_2010_july = len(df_colunns[is_2010 & is_july])
crimes_2010_august = len(df_colunns[is_2010 & is_august])
crimes_2010_september = len(df_colunns[is_2010 & is_september])
crimes_2010_october = len(df_colunns[is_2010 & is_october])
crimes_2010_november = len(df_colunns[is_2010 & is_november])
crimes_2010_december = len(df_colunns[is_2010 & is_december])


crimes_2011_january = len(df_colunns[is_2011 & is_january])
crimes_2011_february = len(df_colunns[is_2011 & is_february])
crimes_2011_march = len(df_colunns[is_2011 & is_march])
crimes_2011_april = len(df_colunns[is_2011 & is_april])
crimes_2011_may = len(df_colunns[is_2011 & is_may])
crimes_2011_june = len(df_colunns[is_2011 & is_june])
crimes_2011_july = len(df_colunns[is_2011 & is_july])
crimes_2011_august = len(df_colunns[is_2011 & is_august])
crimes_2011_september = len(df_colunns[is_2011 & is_september])
crimes_2011_october = len(df_colunns[is_2011 & is_october])
crimes_2011_november = len(df_colunns[is_2011 & is_november])
crimes_2011_december = len(df_colunns[is_2011 & is_december])

crimes_2012_january = len(df_colunns[is_2012 & is_january])
crimes_2012_february = len(df_colunns[is_2012 & is_february])
crimes_2012_march = len(df_colunns[is_2012 & is_march])
crimes_2012_april = len(df_colunns[is_2012 & is_april])
crimes_2012_may = len(df_colunns[is_2012 & is_may])
crimes_2012_june = len(df_colunns[is_2012 & is_june])
crimes_2012_july = len(df_colunns[is_2012 & is_july])
crimes_2012_august = len(df_colunns[is_2012 & is_august])
crimes_2012_september = len(df_colunns[is_2012 & is_september])
crimes_2012_october = len(df_colunns[is_2012 & is_october])
crimes_2012_november = len(df_colunns[is_2012 & is_november])
crimes_2012_december = len(df_colunns[is_2012 & is_december])

crimes_2013_january = len(df_colunns[is_2013 & is_january])
crimes_2013_february = len(df_colunns[is_2013 & is_february])
crimes_2013_march = len(df_colunns[is_2013 & is_march])
crimes_2013_april = len(df_colunns[is_2013 & is_april])
crimes_2013_may = len(df_colunns[is_2013 & is_may])
crimes_2013_june = len(df_colunns[is_2013 & is_june])
crimes_2013_july = len(df_colunns[is_2013 & is_july])
crimes_2013_august = len(df_colunns[is_2013 & is_august])
crimes_2013_september = len(df_colunns[is_2013 & is_september])
crimes_2013_october = len(df_colunns[is_2013 & is_october])
crimes_2013_november = len(df_colunns[is_2013 & is_november])
crimes_2013_december = len(df_colunns[is_2013 & is_december])

crimes_2014_january = len(df_colunns[is_2014 & is_january])
crimes_2014_february = len(df_colunns[is_2014 & is_february])
crimes_2014_march = len(df_colunns[is_2014 & is_march])
crimes_2014_april = len(df_colunns[is_2014 & is_april])
crimes_2014_may = len(df_colunns[is_2014 & is_may])
crimes_2014_june = len(df_colunns[is_2014 & is_june])
crimes_2014_july = len(df_colunns[is_2014 & is_july])
crimes_2014_august = len(df_colunns[is_2014 & is_august])
crimes_2014_september = len(df_colunns[is_2014 & is_september])
crimes_2014_october = len(df_colunns[is_2014 & is_october])
crimes_2014_november = len(df_colunns[is_2014 & is_november])
crimes_2014_december = len(df_colunns[is_2014 & is_december])

crimes_2015_january = len(df_colunns[is_2015 & is_january])
crimes_2015_february = len(df_colunns[is_2015 & is_february])
crimes_2015_march = len(df_colunns[is_2015 & is_march])
crimes_2015_april = len(df_colunns[is_2015 & is_april])
crimes_2015_may = len(df_colunns[is_2015 & is_may])
crimes_2015_june = len(df_colunns[is_2015 & is_june])
crimes_2015_july = len(df_colunns[is_2015 & is_july])
crimes_2015_august = len(df_colunns[is_2015 & is_august])
crimes_2015_september = len(df_colunns[is_2015 & is_september])
crimes_2015_october = len(df_colunns[is_2015 & is_october])
crimes_2015_november = len(df_colunns[is_2015 & is_november])
crimes_2015_december = len(df_colunns[is_2015 & is_december])

crimes_2016_january = len(df_colunns[is_2016 & is_january])
crimes_2016_february = len(df_colunns[is_2016 & is_february])
crimes_2016_march = len(df_colunns[is_2016 & is_march])
crimes_2016_april = len(df_colunns[is_2016 & is_april])
crimes_2016_may = len(df_colunns[is_2016 & is_may])
crimes_2016_june = len(df_colunns[is_2016 & is_june])
crimes_2016_july = len(df_colunns[is_2016 & is_july])
crimes_2016_august = len(df_colunns[is_2016 & is_august])
crimes_2016_september = len(df_colunns[is_2016 & is_september])
crimes_2016_october = len(df_colunns[is_2016 & is_october])
crimes_2016_november = len(df_colunns[is_2016 & is_november])
crimes_2016_december = len(df_colunns[is_2016 & is_december])

crimes_2017_january = len(df_colunns[is_2017 & is_january])
crimes_2017_february = len(df_colunns[is_2017 & is_february])
crimes_2017_march = len(df_colunns[is_2017 & is_march])
crimes_2017_april = len(df_colunns[is_2017 & is_april])
crimes_2017_may = len(df_colunns[is_2017 & is_may])
crimes_2017_june = len(df_colunns[is_2017 & is_june])
crimes_2017_july = len(df_colunns[is_2017 & is_july])
crimes_2017_august = len(df_colunns[is_2017 & is_august])
crimes_2017_september = len(df_colunns[is_2017 & is_september])
crimes_2017_october = len(df_colunns[is_2017 & is_october])
crimes_2017_november = len(df_colunns[is_2017 & is_november])
crimes_2017_december = len(df_colunns[is_2017 & is_december])

crimes_2018_january = len(df_colunns[is_2018 & is_january])
crimes_2018_february = len(df_colunns[is_2018 & is_february])
crimes_2018_march = len(df_colunns[is_2018 & is_march])
crimes_2018_april = len(df_colunns[is_2018 & is_april])
crimes_2018_may = len(df_colunns[is_2018 & is_may])
crimes_2018_june = len(df_colunns[is_2018 & is_june])
crimes_2018_july = len(df_colunns[is_2018 & is_july])
crimes_2018_august = len(df_colunns[is_2018 & is_august])
crimes_2018_september = len(df_colunns[is_2018 & is_september])
crimes_2018_october = len(df_colunns[is_2018 & is_october])
crimes_2018_november = len(df_colunns[is_2018 & is_november])
crimes_2018_december = len(df_colunns[is_2018 & is_december])

plt.figure(figsize=(15, 10))

#--------
plt.title('crimes doing month chicago - 2001')

plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2001_january,crimes_2001_february,crimes_2001_march,crimes_2001_april,crimes_2001_may,crimes_2001_june,crimes_2001_july,
          crimes_2001_august,crimes_2001_september,crimes_2001_october,crimes_2001_november,crimes_2001_december])


plt.savefig(image_path+'chicago - 2001', bbox_inches='tight' )
plt.clf()

#--------

plt.title('crimes doing month chicago - 2002')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2002_january,crimes_2002_february,crimes_2002_march,crimes_2002_april,crimes_2002_may,crimes_2002_june,crimes_2002_july,
          crimes_2002_august,crimes_2002_september,crimes_2002_october,crimes_2002_november,crimes_2002_december])

plt.savefig(image_path+'chicago - 2002', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2003')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2003_january,crimes_2003_february,crimes_2003_march,crimes_2003_april,crimes_2003_may,crimes_2003_june,crimes_2003_july,
          crimes_2003_august,crimes_2003_september,crimes_2003_october,crimes_2003_november,crimes_2003_december])

plt.savefig(image_path+'chicago - 2003', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2004')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2004_january,crimes_2004_february,crimes_2004_march,crimes_2004_april,crimes_2004_may,crimes_2004_june,crimes_2004_july,
          crimes_2004_august,crimes_2004_september,crimes_2004_october,crimes_2004_november,crimes_2004_december])

plt.savefig(image_path+'chicago - 2004', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2005')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2005_january,crimes_2005_february,crimes_2005_march,crimes_2005_april,crimes_2005_may,crimes_2005_june,crimes_2005_july,
          crimes_2005_august,crimes_2005_september,crimes_2005_october,crimes_2005_november,crimes_2005_december])

plt.savefig(image_path+'chicago - 2005', bbox_inches='tight')
plt.clf()


#--------

plt.title('crimes doing month chicago - 2006')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2006_january,crimes_2006_february,crimes_2006_march,crimes_2006_april,crimes_2006_may,crimes_2006_june,crimes_2006_july,
          crimes_2006_august,crimes_2006_september,crimes_2006_october,crimes_2006_november,crimes_2006_december])

plt.savefig(image_path+'chicago - 2006', bbox_inches='tight')
plt.clf()


#--------

plt.title('crimes doing month chicago - 2007')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2007_january,crimes_2007_february,crimes_2007_march,crimes_2007_april,crimes_2007_may,crimes_2007_june,crimes_2007_july,
          crimes_2007_august,crimes_2007_september,crimes_2007_october,crimes_2007_november,crimes_2007_december])

plt.savefig(image_path+'chicago - 2007', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2008')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2008_january,crimes_2008_february,crimes_2008_march,crimes_2008_april,crimes_2008_may,crimes_2008_june,crimes_2008_july,
          crimes_2008_august,crimes_2008_september,crimes_2008_october,crimes_2008_november,crimes_2008_december])

plt.savefig(image_path+'chicago - 2008', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2009')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2009_january,crimes_2009_february,crimes_2009_march,crimes_2009_april,crimes_2009_may,crimes_2009_june,crimes_2009_july,
          crimes_2009_august,crimes_2009_september,crimes_2009_october,crimes_2009_november,crimes_2009_december])

plt.savefig(image_path+'chicago - 2009', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2010')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2010_january,crimes_2010_february,crimes_2010_march,crimes_2010_april,crimes_2010_may,crimes_2010_june,crimes_2010_july,
          crimes_2010_august,crimes_2010_september,crimes_2010_october,crimes_2010_november,crimes_2010_december])

plt.savefig(image_path+'chicago - 2010', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2011')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2011_january,crimes_2011_february,crimes_2011_march,crimes_2011_april,crimes_2011_may,crimes_2011_june,crimes_2011_july,
          crimes_2011_august,crimes_2011_september,crimes_2011_october,crimes_2011_november,crimes_2011_december])

plt.savefig(image_path+'chicago - 2011', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2012')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2012_january,crimes_2012_february,crimes_2012_march,crimes_2012_april,crimes_2012_may,crimes_2012_june,crimes_2012_july,
          crimes_2012_august,crimes_2012_september,crimes_2012_october,crimes_2012_november,crimes_2012_december])

plt.savefig(image_path+'chicago - 2012', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2013')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2013_january,crimes_2013_february,crimes_2013_march,crimes_2013_april,crimes_2013_may,crimes_2013_june,crimes_2013_july,
          crimes_2013_august,crimes_2013_september,crimes_2013_october,crimes_2013_november,crimes_2013_december])

plt.savefig(image_path+'chicago - 2013', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2014')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2014_january,crimes_2014_february,crimes_2014_march,crimes_2014_april,crimes_2014_may,crimes_2014_june,crimes_2014_july,
          crimes_2014_august,crimes_2014_september,crimes_2014_october,crimes_2014_november,crimes_2014_december])

plt.savefig(image_path+'chicago - 2014', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2015')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2015_january,crimes_2015_february,crimes_2015_march,crimes_2015_april,crimes_2015_may,crimes_2015_june,crimes_2015_july,
          crimes_2015_august,crimes_2015_september,crimes_2015_october,crimes_2015_november,crimes_2015_december])

plt.savefig(image_path+'chicago - 2015', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2016')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2016_january,crimes_2016_february,crimes_2016_march,crimes_2016_april,crimes_2016_may,crimes_2016_june,crimes_2016_july,
          crimes_2016_august,crimes_2016_september,crimes_2016_october,crimes_2016_november,crimes_2016_december])

plt.savefig(image_path+'chicago - 2016', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2017')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2017_january,crimes_2017_february,crimes_2017_march,crimes_2017_april,crimes_2017_may,crimes_2017_june,crimes_2017_july,
          crimes_2017_august,crimes_2017_september,crimes_2017_october,crimes_2017_november,crimes_2017_december])

plt.savefig(image_path+'chicago - 2017', bbox_inches='tight')
plt.clf()

#--------

plt.title('crimes doing month chicago - 2018')
plt.plot(['january','february','march','april','may','june','july','august','september','october','november','december'],
         [crimes_2018_january,crimes_2018_february,crimes_2018_march,crimes_2018_april,crimes_2018_may,crimes_2018_june,crimes_2018_july,
          crimes_2018_august,crimes_2018_september,crimes_2018_october,crimes_2018_november,crimes_2018_december])

plt.savefig(image_path+'chicago - 2018', bbox_inches='tight')
plt.clf()

#--------



