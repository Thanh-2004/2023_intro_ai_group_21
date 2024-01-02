from AIProjectData import *

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

import Astar_1step
import Astar_2step
import GreedyBFSforAI
import Greedy
import Bidirectional_Astar

def selected(path):
    x_point = []
    y_point = []
    level = 0
    for i in range (1, len(path) - 1):
        if "Station" not in path[i]:
            level += 1
            x_point.append(data.loc[p.number_to_words(p.ordinal(level)) + 'Level'].loc[path[i]]["Latitude"])
            y_point.append(data.loc[p.number_to_words(p.ordinal(level)) + 'Level'].loc[path[i]]["Longitude"])
        else:
            x_point.append(data.loc["Stations"].loc[path[i]]["Latitude"])
            y_point.append(data.loc["Stations"].loc[path[i]]["Longitude"])

    x_point.insert(0,start[0])
    y_point.insert(0,start[1])
    x_point.append(finish[0])
    y_point.append(finish[1])
    return x_point,y_point

def scatter(ax):
    # colors = list(mcolors.TABLEAU_COLORS.values())
    # colors.extend(['black', '#9400D3', '#FFFF00'])
    colors = list(mcolors.CSS4_COLORS.values())
    random.shuffle(colors)
    ax.scatter(start[0], start[1], c = colors[0], label = 'Start', edgecolors= 'red', linewidths=0.5)
    ax.scatter(finish[0], finish[1], c = colors[1], label = 'Finish', edgecolors='red', linewidths=0.5)

    for i in range(NumberOfLevelsandStations):
        if i != NumberOfLevelsandStations - 1:
            
            ax.scatter([LevelPoints[i][j][0] for j in range(NumberLevel[i])], [LevelPoints[i][j][1] for j in range(NumberLevel[i])], c = colors[i+2],  edgecolors= 'black', linewidths=0.5)
        else:
            ax.scatter([LevelPoints[i][j][0] for j in range(NumberLevel[i])], [LevelPoints[i][j][1] for j in range(NumberLevel[i])], c = colors[i+2], linewidths=0.5)
    return scatter



path1 = Astar_1step.path
path2 =  Astar_2step.path
path3 = GreedyBFSforAI.path
path4 = Greedy.path
path5 = Bidirectional_Astar.path
Paths = [path1, path2, path3, path4, path5]
names = ["Astar_1step", "Astar_2step", "GreedyBFSforAI", "Greedy", "Bidirectional_Astar"]
# Dữ liệu giả định


# Tạo subplot với 2 hàng và 2 cột
fig, axes = plt.subplots(1,5)

# Hàm được gọi mỗi frame của animation
def update(frame):
    if frame > 0:
        # Lặp qua từng subplot
        for i, ax in enumerate(axes.flat):
            # Chọn ngẫu nhiên số điểm từ dữ liệu
            selected_x, selected_y = selected(Paths[i])

            # Vẽ đường nối giữa các điểm
            lines[i].set_data(selected_x[:frame+1], selected_y[:frame+1])
            lines[i].set_color('red')
            lines[i].set_alpha(0.8)
    return lines

# Vẽ các điểm trên tất cả các subplot
for i, ax in enumerate(axes.flat):
    scatter = scatter(ax)
    ax.set_title(f'{names[i]}', fontsize=10)

# Khởi tạo đường nối cho từng subplot
lines = [ax.plot([], [], marker='o')[0] for ax in axes.flat]

plt.subplots_adjust(wspace=0.5, hspace=0.5)
# Thiết lập animation
ani = animation.FuncAnimation(fig, update, frames=max(5, 10, 15, 20), interval=500, blit=True)

# Hiển thị chú thích
for ax in axes.flat:
    ax.legend()

# Hiển thị biểu đồ
plt.show()

distance1 = Astar_1step.distance
distance2 =  Astar_2step.distance
distance3 = GreedyBFSforAI.distance
distance4 = Greedy.distance
distance5 = Bidirectional_Astar.distance
Distance = [distance1, distance2, distance3, distance4, distance5]


node_expanded1 = Astar_1step.node_expanded
node_expanded2 =  Astar_2step.node_expanded
node_expanded3 = GreedyBFSforAI.node_expanded
node_expanded4 = Greedy.node_expanded
node_expanded5 = Bidirectional_Astar.node_expanded
Nodes = [node_expanded1,node_expanded2, node_expanded3, node_expanded4, node_expanded5]


# Đường dẫn đến tệp văn bản
file_path = "output.txt"

# Mở tệp với chế độ 'w' (ghi), nếu tệp không tồn tại, nó sẽ được tạo mới
with open(file_path, 'w') as file:
    file.write(f"Output for {NumberOfLevelsandStations - 1} levels and fuel capacity is {fuel_capacity}")
    file.write("\n")
    for i in range (5):
        file.write(f"{names[i]}: \n" + f"Path: {Paths[i]} \n" + f"Distance travelled: {Distance[i]} \n" + f"Node Expanded: {Nodes[i]} \n" )
        file.write("\n")
        file.write("\n")




