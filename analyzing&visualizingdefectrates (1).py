# -*- coding: utf-8 -*-
"""Analyzing&VisualizingDefectRates.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WUL0ISr2QzGlsbNe0eBhwAjPWETtk4ni
"""

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt

uploaded = files.upload()

data = pd.read_csv("supply_chain_data.csv")

data.head()

defect_rate_by_product = data.groupby("Product type")["Defect rates"].mean()

print("Defect rates by product type:")
print(defect_rate_by_product)

plt.figure(figsize=(10,6))
defect_rate_by_product.plot(kind="bar",color='skyblue')
plt.title("Defect Rates by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Mean Defect Rate")
plt.xticks(rotation=45)
plt.show()