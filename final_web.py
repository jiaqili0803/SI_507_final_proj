import json

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests

######################################################## user chioce from Tree 
# whether they want other two data
# 1. solar_rad: Average solar radiation (W/M^2) 日照
# 2. max_uv: Maximum UV Index (0-11+) 辐射

yesBag = ["Yes", 'yes', 'Y', 'y', 'Yup', 'yup', 'Sure', 'sure']

# tree example:
#                  Question1
#                  /       \
#                 Y         N
#                /           \
#             Ques2         Ques2
#            /     \        /    \
#         (Y, Y)  (Y, N)   (N, Y)  (N, N)
# 
# (Q1, (Q2, (Y,Y), (Y,N)), (Q2, (N,Y), (N,N))

# 1. solar_rad: Average solar radiation (W/M^2) 日照
# 2. max_uv: Maximum UV Index (0-11+) 辐射

quesTree = \
    ("Question1: Do you want to know solar radiation?",
        ("Question2: Do you want to know UV Index?",
            ("Yes", "Yes"),
            ("Yes", "No")),
        ("Question2: Do you want to know UV Index??",
            ("No", "Yes"),
            ("No", "No")))

def printTree(tree, level, prefix = '', bend = ''):
    if level == 2:
        print(f'{prefix}{bend}{tree}')

    else: 
        text, left, right = tree
        print(f'{prefix}{bend}{text}')
        if bend == '+-':
            prefix = prefix + '| '
        elif bend == '`-':
            prefix = prefix + '| '
        printTree(left, level+1, prefix, '+-')
        printTree(right, level+1, prefix, '`-')
        

def yes(prompt):
    ans = input(prompt + "  ")
    ans = ans.strip()
    if ans in yesBag:
        return True
    return False

def playLeaf(tree, level):
    if level == 2:
        # output = yes(tree[0])
        return tree

    text, left, right = tree
    ans = yes(text)
    if ans == True:
        output = playLeaf(left, level+1)
    else:
        output = playLeaf(right, level+1)
    
    return output


def main():
    op = playLeaf(quesTree, 0)
    print(op)
    #print(type(op))
    choice1 = op[0]
    choice2 = op[1]
    print('                         ')
    print('#########################')
    print('######## The Tree #######')
    print('#########################')
    print('                         ')
    printTree(quesTree, 0)
    return choice1, choice2

# if __name__ == '__main__':
#     main()
     
    
        

############################################################ input
user_input_city = input('Which city do you live ? : ')
user_input_state = input('Which state do you live ? : ')
user_input_start_date = input('Start Date you want to know ?  (e.g.2021-8-16) : ')
user_input_end_date = input('End Date you want to know ?  (e.g.2021-8-16) : ')



############################################################ historical weather
weather_url =f'http://api.weatherbit.io/v2.0/history/daily?&city={user_input_city}&start_date={user_input_start_date}&end_date={user_input_end_date}&key=8d70ed4831f6452cbb99c2a659d5ff43'

response = requests.get(weather_url)
text = response.text
results_object = json.loads(text)  # dict
result = results_object["data"]
#print(json.dumps(result, indent=4))

#### write to json file
js = json.dumps(results_object, indent=4)
f1 = open(r'C:\Users\Jiaqi\Desktop\SI_507\final_proj\json_file\weather_json.json', 'w')
f1.write(js)
f1.close()

######################################################## plotly (4+2 category) 

# wind_spd: Average wind speed (Default m/s) 风速度
wind_spd = []
date_time = []
for i in range(len(results_object['data'])):
    wind_spd.append(result[i]["wind_spd"])
    date_time.append(result[i]["datetime"])
#print(result[i]["wind_spd"])

fig = go.Figure()
fig.add_trace(go.Scatter(x=date_time, y=wind_spd, mode='lines+markers', name='Average wind speed (Default m/s)'))



fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    # yaxis=dict(
    #     showgrid=False,
    #     zeroline=False,
    #     showline=False,
    #     showticklabels=False,
    # ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    # showlegend=False,
    plot_bgcolor='white'
)

# Title
annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Average wind speed (Default m/s)',
                              font=dict(family='Arial',
                                        size=30,
                                        color='rgb(37,37,37)'),
                              showarrow=False))

fig.update_layout(annotations=annotations)

fig.show()


# temp: Average temperature (default Celcius) 温度

temp = []
date_time = []
for i in range(len(results_object['data'])):
    temp.append(result[i]["temp"])
    date_time.append(result[i]["datetime"])
#print(result[i]["temp"])

fig = go.Figure()
fig.add_trace(go.Scatter(x=date_time, y=temp, mode='lines+markers', name='Average temperature (default Celcius)'))



fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    # showlegend=False,
    plot_bgcolor='white'
)

# Title
annotations = []
annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                              xanchor='left', yanchor='bottom',
                              text='Average temperature (default Celcius)',
                              font=dict(family='Arial',
                                        size=30,
                                        color='black'),
                              showarrow=False))

fig.update_layout(annotations=annotations)

fig.show()


# rh: Average relative humidity (%) 湿度

rh = []
date_time = []
for i in range(len(results_object['data'])):
    rh.append(result[i]["rh"])
    date_time.append(result[i]["datetime"])
#print(result[i]["rh"])

fig = go.Figure(data=[go.Bar(x=date_time, y=rh, marker_color='pink',)])

fig.update_layout(title_text='Average relative humidity (%) ')

fig.show()


# precip_gpm: Accumulated precipitation 降水


precip_gpm = []
date_time = []
for i in range(len(results_object['data'])):
    precip_gpm.append(result[i]["precip_gpm"])
    date_time.append(result[i]["datetime"])

fig = go.Figure(data=[go.Bar(x=date_time, y=precip_gpm, marker_color='gold')])

fig.update_layout(title_text='Accumulated precipitation')

fig.show()


 
# solar_rad: Average solar radiation (W/M^2) 日照
choices = main()

if choices[0] == 'Yes':
    solar_rad = []
    date_time = []
    for i in range(len(results_object['data'])):
        solar_rad.append(result[i]["solar_rad"])
        date_time.append(result[i]["datetime"])
    #print(result[i]["solar_rad"])

    fig = go.Figure(data=[go.Bar(x=date_time, y=solar_rad, marker_color='lightcoral')])

    fig.update_layout(title_text='Average solar radiation (W/M^2) ')

    fig.show()
else:
    print('')
        
# max_uv: Maximum UV Index (0-11+) 辐射
if choices[1] == 'Yes':
    max_uv = []
    date_time = []
    for i in range(len(results_object['data'])):
        max_uv.append(result[i]["max_uv"])
        date_time.append(result[i]["datetime"])
    #print(result[i]["max_uv"])

    fig = go.Figure(data=[go.Bar(x=date_time, y=max_uv, marker_color='brown')])

    fig.update_layout(title_text='Maximum UV Index (0-11+) ')

    fig.show()
else:
    print('')


############################################################### air quality

air_url = f'http://api.airvisual.com/v2/city?city={user_input_city}&state={user_input_state}&country=USA&key=99c4feb5-a1bd-48b3-a45a-0f884d9359b8'


response = requests.get(air_url)
text = response.text
results_object = json.loads(text)  # dict
result = results_object["data"]
AQI = result["current"]["pollution"]["aqius"]
#print(json.dumps(result, indent=4))
print(f'The AQI for your position now is : {AQI}')
print('                                            ')

######## write to json file

js = json.dumps(results_object, indent=4)
f2 = open(r'C:\Users\Jiaqi\Desktop\SI_507\final_proj\json_file\air_json.json', 'w')
f2.write(js)
f2.close()
   

  





