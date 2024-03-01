import pandas as pd
import plotly.express as px

df = pd.read_csv("FF_SR_data.csv")
categories = pd.read_csv("food_category_id table.csv")


df = df[["food_category_id","FF Food description","SR Food description", "FF_Component" , "SR_Component", "SR Mean per 100g", "FF Mean per 100g"]]
srmean = df['SR Mean per 100g']
ffmean = df['FF Mean per 100g']

srmean = pd.to_numeric(srmean,errors='coerce')
ffmean = pd.to_numeric(ffmean,errors='coerce')

df['Mean Difference'] = ((srmean.fillna(0) - ffmean.fillna(0))/srmean) * 100

df.sort_values('Mean Difference',ascending=False).reset_index().to_csv('allmeandiffsorted.csv')

mean_sorted = pd.read_csv('allmeandiffsorted.csv')

calories = mean_sorted[mean_sorted['FF_Component'] == 'Energy']
calcium = mean_sorted[mean_sorted['FF_Component'] == 'Calcium, Ca']
water = mean_sorted[mean_sorted['FF_Component'] == 'Water']
protein = mean_sorted[mean_sorted['FF_Component'] == 'Protein']
fat = mean_sorted[mean_sorted['FF_Component'] == 'Total lipid (fat)']

foodgroups_calories = calories['Mean Difference'].groupby(calories['food_category_id'])
calorie_means = foodgroups_calories.mean().to_frame(name='Mean').reset_index()

foodgroups_calcium = calcium['Mean Difference'].groupby(calcium['food_category_id'])
calcium_means = foodgroups_calcium.mean().to_frame(name='Mean').reset_index()

foodgroups_water = water['Mean Difference'].groupby(water['food_category_id'])
water_means = foodgroups_water.mean().to_frame(name='Mean').reset_index()

foodgroups_protein = protein['Mean Difference'].groupby(protein['food_category_id'])
protein_means = foodgroups_protein.mean().to_frame(name='Mean').reset_index()

foodgroups_fat = fat['Mean Difference'].groupby(fat['food_category_id'])
fat_means = foodgroups_fat.mean().to_frame(name='Mean').reset_index()

mergedcalories = categories.merge(calorie_means, how='inner')
mergedcalcium = categories.merge(calcium_means, how='inner')
mergedwater = categories.merge(water_means,how='inner')
mergedprotein = categories.merge(protein_means,how='inner')
mergedfat = categories.merge(fat_means,how='inner')

fig = px.bar(mergedcalcium, x="description", y="Mean",
             title="Mean Difference of Calcium Components by Food Group",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="description", 
             hover_name="description",
             template="plotly",
             width=1000, height=600)

fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    bargap=0.01
)

fig.show()

fig = px.bar(mergedcalories, x="description", y="Mean",
             title="Mean Difference of Calories by Food Group",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="description", 
             hover_name="description",
             template="plotly",
             width=1000, height=600)

fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    bargap=0.01
)

fig.show()

fig = px.bar(mergedwater, x="description", y="Mean",
             title="Mean Difference of Water Content by Food Group",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="description", 
             hover_name="description",
             template="plotly",
             width=1000, height=600)

fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    bargap=0.01
)

fig.show()

fig = px.bar(mergedprotein, x="description", y="Mean",
             title="Mean Difference of Protein by Food Group",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="description", 
             hover_name="description",
             template="plotly",
             width=1000, height=600)

fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    bargap=0.01
)

fig.show()

fig = px.bar(mergedfat, x="description", y="Mean",
             title="Mean Difference of Fat by Food Group",
             labels={"Mean Difference": "Mean Difference (g/100g)"},
             color="description", 
             hover_name="description",
             template="plotly",
             width=1000, height=600)

fig.update_layout(
    xaxis=dict(title="Food Description"),
    yaxis=dict(title="Mean Difference (g/100g)"),
    legend_title="Food Description",
    font=dict(family="Arial", size=12, color="black"),
    title_font=dict(size=20),
    bargap=0.01
)

fig.show()