import pandas as pd 
import plotly.express as px
import re

with open('fruitsonly.csv', "w") as output_file:
    with open("FF_SR_data.csv", 'r') as fh:
        for line in fh:
            match = re.findall(r'^[0-9]*,[0-9]*,9,', line)
            for s in match:
                output_file.write(line)


df = pd.read_csv("fruitsonly.csv")

df = df[["FF Food description","SR Food description", "FF_Component" , "SR_Component", "SR Mean per 100g", "FF Mean per 100g"]]

df['Mean Difference'] = (df['SR Mean per 100g'] - df['FF Mean per 100g'])


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

#region Vitamin A

VitA = df[df['FF_Component'] == 'Vitamin A, RAE'] 

fig = px.bar(VitA, x="FF Food description", y="Mean Difference",
             title="Mean Difference of Vitamin A Components",
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

VitB = df[df['FF_Component'] == 'Vitamin B-6']


fig = px.bar(VitB, x="FF Food description", y="Mean Difference",
             title="Mean Difference of Vitamin B Components",
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

