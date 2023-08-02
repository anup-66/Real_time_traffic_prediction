import codecs

import requests
import xml.etree.ElementTree as E
response = requests.get("https://informo.madrid.es/informo/tmadrid/pm.xml")
print(response)

# Check if the request was successful
if response.status_code == 200:
    # Get the XML content from the response
    xml_content = response.text

    # Save the XML content to a file
    # with codecs.open('response.xml', 'w',encoding='utf-8-sig') as file:
    #     file.write(xml_content)

    print("XML response saved to response.xml")
else:
    print("Error: API request failed with status code", response.status_code)

import xml.etree.ElementTree as ET

import numpy as np
import pandas as pd

# Parse the XML content
with codecs.open("response.xml",'r',encoding='utf-8-sig') as f:
    xml_content = f.read()
# print(xml_content)
root = ET.fromstring(xml_content)

# Extract data from XML and create a table
data = []
for pm in root.findall('pm'):
    item = {}
    item['idelem'] = pm.find('idelem').text if pm.find('idelem') is not None else ''
    item['descripcion'] = pm.find('descripcion').text if pm.find('descripcion') is not None else ''
    item['accesoAsociado'] = pm.find('accesoAsociado').text if pm.find('accesoAsociado') is not None else ''
    item['intensidad'] = pm.find('intensidad').text if pm.find('intensidad') is not None else ''
    item['ocupacion'] = pm.find('ocupacion').text if pm.find('ocupacion') is not None else ''
    item['carga'] = pm.find('carga').text if pm.find('carga') is not None else ''
    item['nivelServicio'] = pm.find('nivelServicio').text if pm.find('nivelServicio') is not None else ''
    item['intensidadSat'] = pm.find('intensidadSat').text if pm.find('intensidadSat') is not None else ''
    item['error'] = pm.find('error').text if pm.find('error') is not None else ''
    subarea_element = pm.find('.//subarea')  # Adjusted XPath expression
    item['subarea'] = subarea_element.text if subarea_element is not None else None
    item['st_x'] = pm.find('st_x').text if pm.find('st_x') is not None else ''
    item['st_y'] = pm.find('st_y').text if pm.find('st_y') is not None else ''
    data.append(item)

pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)
df = pd.DataFrame(data)
df = df.dropna()

df['idelem'] = df['idelem'].apply(lambda x:int(x))
df['descripcion'] = df['descripcion'].apply(lambda s: s.lower() if isinstance(s, str) else s)
# df = df.sort_values(by='descripcion')
df = df.sort_values(by='descripcion',ascending=True)
# print(df[' descripcion '])
# df = pd.DataFrame({" descripcion ":["a","a","b","b","c","c","c"]})
groupd = df.groupby(df['descripcion'].str[:10])
List = []
for i,j in groupd:
    List.append(j)
j=0
# print(len(List))
for i in List:
    # i.
    if len(i) > 5:
        print(i.head())
    # print(i['descripcion'].head())
    j += 1
    if j == 50:
        break


# print(df['descripcion'].sort_values())
# print(df[["intensidad",'subarea']])
