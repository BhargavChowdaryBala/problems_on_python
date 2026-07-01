import random

sample_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]
sample_jobs = ["Manager", "Developer", "Designer", "Analyst", "HR Specialist", "QA Engineer"]

n = int(input("Enter n (number of employees): "))

d = {}

for i in range(1, n + 1):
    
    name = random.choice(sample_names)
    job = random.choice(sample_jobs)
    
    salary = random.randint(40000, 120000)
    
    d[i] = {
        "name": name,
        "job": job,
        "salary": salary
    }


print("\nAll employee details (Automatically Generated):")
for emp_id, info in d.items():
    print(f"ID {emp_id}: {info}")


search_name = input("\nEnter employee name to display details: ")

found = False
for emp_id, info in d.items():
    if info["name"].lower() == search_name.lower():  
        print(f"\nEmployee details for '{search_name}':")
        print({emp_id: info})
        found = True
        break

if not found:
    print(f"No employee found with name '{search_name}'.")