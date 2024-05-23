import matplotlib.pyplot as plt
import numpy as np

# 定义活动请求
activity_requests = [
    {'id': 1, 'type': '社交活动', 'scale': '大', 'duration': 1, 'day': 0, 'time_slot': (9, 10)},
    {'id': 2, 'type': '会议', 'scale': '小', 'duration': 2, 'day': 0, 'time_slot': (11, 13)},
    {'id': 3, 'type': '研讨会', 'scale': '中', 'duration': 1, 'day': 1, 'time_slot': (14, 15)},
    {'id': 4, 'type': '培训', 'scale': '小', 'duration': 1, 'day': 2, 'time_slot': (10, 11)},
    {'id': 5, 'type': '社交活动', 'scale': '中', 'duration': 2, 'day': 1, 'time_slot': (16, 18)},
    {'id': 6, 'type': '会议', 'scale': '大', 'duration': 1, 'day': 2, 'time_slot': (9, 10)},
    {'id': 7, 'type': '研讨会', 'scale': '小', 'duration': 2, 'day': 1, 'time_slot': (8, 10)},
    {'id': 8, 'type': '培训', 'scale': '中', 'duration': 1, 'day': 0, 'time_slot': (15, 16)},
    {'id': 9, 'type': '社交活动', 'scale': '小', 'duration': 1, 'day': 2, 'time_slot': (13, 14)},
    {'id': 10, 'type': '会议', 'scale': '中', 'duration': 2, 'day': 0, 'time_slot': (17, 19)},
    {'id': 11, 'type': '研讨会', 'scale': '大', 'duration': 1, 'day': 1, 'time_slot': (10, 11)},
    {'id': 12, 'type': '培训', 'scale': '小', 'duration': 1, 'day': 2, 'time_slot': (12, 13)},
    {'id': 13, 'type': '社交活动', 'scale': '大', 'duration': 2, 'day': 1, 'time_slot': (8, 10)},
    {'id': 14, 'type': '会议', 'scale': '中', 'duration': 1, 'day': 0, 'time_slot': (9, 10)},
    {'id': 15, 'type': '研讨会', 'scale': '小', 'duration': 1, 'day': 2, 'time_slot': (11, 12)},
    {'id': 16, 'type': '培训', 'scale': '中', 'duration': 2, 'day': 0, 'time_slot': (13, 15)},
    {'id': 17, 'type': '社交活动', 'scale': '小', 'duration': 1, 'day': 1, 'time_slot': (10, 11)},
    {'id': 18, 'type': '会议', 'scale': '大', 'duration': 1, 'day': 2, 'time_slot': (14, 15)},
    {'id': 19, 'type': '研讨会', 'scale': '中', 'duration': 1, 'day': 1, 'time_slot': (9, 10)},
    {'id': 20, 'type': '培训', 'scale': '小', 'duration': 1, 'day': 0, 'time_slot': (8, 9)}
]


# 有效时间区域（每三天，每天8点到20点，每小时一个时间段）
days = 3
hours_per_day = 12  # 从8点到20点
time_slots = [(d, h) for d in range(days) for h in range(8, 20)]

# 创建一个空白矩阵用于可视化
time_slot_matrix = np.zeros((days * hours_per_day, len(activity_requests)))

# 填充矩阵
for i, request in enumerate(activity_requests):
    day = request['day']
    start_hour, end_hour = request['time_slot']
    for hour in range(start_hour, end_hour):
        row_index = day * hours_per_day + (hour - 8)
        time_slot_matrix[row_index, i] = 1

# 可视化
fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.matshow(time_slot_matrix, cmap='viridis')

# 设置坐标轴
ax.set_xticks(np.arange(len(activity_requests)))
ax.set_xticklabels([f"Activity {req['id']}" for req in activity_requests], rotation=45)
ax.set_yticks(np.arange(days * hours_per_day))
ax.set_yticklabels([f"Day {d}, {h}:00" for d in range(days) for h in range(8, 20)])

# 添加颜色条
cbar = fig.colorbar(cax)
cbar.set_label('Activity Occupancy')

plt.title('Time Slot Constraints Visualization')
plt.xlabel('Activity Requests')
plt.ylabel('Time Slots (Days and Hours)')
plt.show()