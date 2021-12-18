# SI_507_final_proj
The main part is final_web.py. Just open and run it, the interface will begin and you can interact with it via the terminal command line. finalTree.py is just a reference to our tree code. 

During the interaction, your replies to some questions will generate a Tree of your answer data. And the Tree data will be used to determine the data visualization pics for you.

To run the code, you need to use an API key. My API key is put in the code, but has limitations with a free account to access these 2 Web APIs. You can also create your own key by registering on two API websites:

1. https://www.weatherbit.io/api/weather-history-daily

2. https://api-docs.iqair.com/?version=latest 

To run this program, you should have the numpy, request, and plotly graph objects packages installed. 

Also, the program will automatically save the json.file of the data you collected and update it in the folder of json_file.

About the Tree data structure:
During the interaction, your replies to some questions will generate a Tree of your answer data. And the Tree data will be used to determine the data visualization pics for you.
Example:
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

#########################
######## The Tree #######
#########################

Question1: Do you want to know solar radiation?
+-Question2: Do you want to know UV Index?
| +-('Yes', 'Yes')
| `-('Yes', 'No')
`-Question2: Do you want to know UV Index??
| +-('No', 'Yes')
| `-('No', 'No')
![image](https://user-images.githubusercontent.com/40383000/146625929-520f971c-4010-411f-b535-7a7aa1341f24.png)

