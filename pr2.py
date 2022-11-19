# 👉 2. Create a dictionary of any 7 Indian states 
# and their capitals. 
# Write this into a JSON file.
import json
state_capital={"Odisha":"Bhubaneswar", "West Bengal":"Kolkata", 
"Punjab":"Chandigarh", "Bihar":"Patna", 
"Uttar Pradesh":"Kanpur", "Karnataka":"Bengaluru", "Maharastra":"Mumbai"}

with open("State_Capital.json","w") as S_C:
    json.dump(state_capital,S_C)

import json
with open("State_Capital.json","r") as S_C_read:
    x= json.load(S_C_read)
    for k,v in x.items():
        print(k,":",v)