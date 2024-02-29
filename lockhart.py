import pandas as pd
import plotly.express as px
import re
import csv
# fh = pd.read_csv("FF_SR_data.csv")
# cols = fh.columns
# category = fh['food_category_id']

# for rows in category:                   #if the category number is 5 then print the sr mean
#     if rows == 5:
#         print(fh['SR Mean per 100g'])
# pattern = r'^[0-9]*,[0-9]*,5,'
# with open('poultryonly.csv',"w") as output_file:
#     with open("FF_SR_data.csv",'r') as fh:
#         for line in fh:
#             match = re.findall(pattern, line)
#             for s in match:
#                 output_file.write(line)


##### right now it does not have column headers so doesn't know 'FF_Component'

df = pd.read_csv("poultry.csv")
#print(df.head())
df = df[["FF Food description","SR Food description", "FF_Component" , "SR_Component", "SR Mean per 100g", "FF Mean per 100g"]]

df['Mean Difference'] = abs(df['SR Mean per 100g'] - df['FF Mean per 100g'])

print(df['FF_Component'])
#region Calcium

calcium = df[df['FF_Component'] == 'Calcium, Ca']

fig = px.bar(calcium, x="FF Food description", y="Mean Difference",
             title="Mean Difference of Calcium Components",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="FF Food description", 
             barmode="group",
             hover_name="FF Food description",
             template="plotly",
             width=1000, height=600)

# Update layout for better aesthetics
fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
fig.update_traces(marker=dict(line=dict(width=0.2)))
fig.show()
# endregion

#region Water

VitA = df[df['FF_Component'] == 'Water'] 

fig = px.bar(VitA, x="FF Food description", y="Mean Difference",
             title="Mean Difference of Water Components",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="FF Food description", 
             barmode="group",
             hover_name="FF Food description",
             template="plotly",
             width=1000, height=600)

# Update layout for better aesthetics
fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
fig.update_traces(marker=dict(line=dict(width=0.2)))
fig.show()
# endregion

#region Vitamin B 

VitB = df[df['FF_Component'] == 'Cholesterol']


fig = px.bar(VitB, x="FF Food description", y="Mean Difference",
             title="Mean Difference of Choloesterol Components",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="FF Food description", 
             barmode="group",
             hover_name="FF Food description",
             template="plotly",
             width=1000, height=600)

fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
fig.update_traces(marker=dict(line=dict(width=0.2)))
fig.show()
# endregion

#region Phosphorus

phos = df[df['FF_Component'] == "Phosphorus, P"] 


fig = px.bar(phos, x="FF Food description", y="Mean Difference",
             title="Mean Difference of Phosphorus Components",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="FF Food description", 
             barmode="group",
             hover_name="FF Food description",
             template="plotly",
             width=1000, height=600)

# Update layout for better aesthetics
fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
fig.update_traces(marker=dict(line=dict(width=0.2)))
fig.show()

# endregion

#region Protein

protein = df[df['FF_Component'] == 'Protein']


fig = px.bar(protein, x="FF Food description", y="Mean Difference",
             title="Mean Difference of Protein Components",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="FF Food description", 
             barmode="group",
             hover_name="FF Food description",
             template="plotly",
             width=1000, height=600)

# Update layout for better aesthetics
fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
)
fig.update_traces(marker=dict(line=dict(width=0.2)))
fig.show()

# endregion
