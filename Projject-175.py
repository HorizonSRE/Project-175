import matplotlib.pyplot as plt
import psutil
app_name_dict = {}
count = 0
for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    if count <= 6:
        name = process.info['name']
        cpu_usage = process.info['cpu_percent']
        print(f"Process {count + 1}: {name} (CPU Usage: {cpu_usage:.2f}%)")
        app_name_dict.update({name: cpu_usage})
        count += 1
keymax = max(app_name_dict, key=app_name_dict.get)
keymin = min(app_name_dict, key=app_name_dict.get)
name_list = [keymax, keymin]
app = app_name_dict.values()
max_app = max(app)
min_app = min(app)
max_min_list = [max_app, min_app]
plt.figure(figsize=(8, 5))  
plt.xlabel("Applications")
plt.ylabel("CPU Usage (%)")
plt.bar(name_list, max_min_list, width=0.4, color=['red', 'green'])  
plt.show()
