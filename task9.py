
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("employees.csv")

#Creating a folder to save all charts

output_folder = Path("charts")
output_folder.mkdir(exist_ok=True)


#Average Salary by Department (Bar chart)

avg_sal = df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
bars = plt.bar(avg_sal.index, avg_sal.values)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

# Displaying salary values on the bar
plt.bar_label(bars, fmt="%.2f", padding=3)

plt.tight_layout()
plt.savefig(output_folder / "1_bar_chart.png", dpi=300)
plt.close()


#Salary Histogram with 5 bins

plt.figure(figsize=(8, 5))

plt.hist(df["salary"].dropna(), bins=5, edgecolor="red")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.tight_layout()
plt.savefig(output_folder / "2_histogram.png", dpi=300)
plt.close()



#Employee ID vs Salary using legend

plt.figure(figsize=(8, 5))

for department, group in df.groupby("department"):
    plt.scatter(
        group["id"],
        group["salary"],
        label=department
    )

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")

plt.tight_layout()
plt.savefig(output_folder / "3_legend.png", dpi=300)
plt.close()


#Monthly Sales using Line Chart

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.figure(figsize=(8, 5))

plt.plot(months, sales, marker="o", label="Monthly Sales")

plt.title("Monthly Sales (Jan to Jun)")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()


plt.tight_layout()
plt.savefig(output_folder / "4_line_chart.png", dpi=300)
plt.close()

print("All charts are saved to the charts folder...!")
