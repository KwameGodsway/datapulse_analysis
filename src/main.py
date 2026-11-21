import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone"],
    "Sales": [1200, 800, 450, 1100, 750],
    "Region": ["Accra", "Kumasi", "Accra", "Takoradi", "Accra"]
}

df = pd.DataFrame(data)

# Group by Product
sales_by_product = df.groupby("Product")["Sales"].sum()
print(sales_by_product)

# Chart
sales_by_product.plot(kind="bar", title="Sales by Product")
plt.ylabel("Sales (GHS)")
plt.tight_layout()
plt.savefig("outputs/sales_by_product.png")
plt.show()
print("Chart saved to outputs/sales_by_product.png")