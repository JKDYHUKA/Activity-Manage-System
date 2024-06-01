# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:07:35 2024

@author: szy
"""

import numpy as np
from scipy.optimize import linprog

# 设定活动类型和优先级
activity_priority = {
    '会议': 1,
    '研讨会': 2,
    '培训': 3,
    '社交活动': 4
}

# 规定活动规模和场地大小
activity_scale = {
    '小': 50,
    '中': 100,
    '大': 200
}
#定义场地
activity_venues={
    '逸夫楼105':'大',
    #'逸夫楼107':'大',
    '逸夫楼104':'中',
    '逸夫楼101':'中',
    '逸夫楼103':'小',
    '逸夫楼203':'小',
    }
# 场地数量
venues_count = {
    '小': 0,
    '中': 0,
    '大': 0
}
for venue_size in activity_venues.values():
    venues_count[venue_size] += 1

#场地归类
venues_by_size={'小': [], '中': [], '大': []}
for venue,size in activity_venues.items():
    venues_by_size[size].append(venue)

# 有效时间区域（8点到20点）
time_slots = [(i, i+1) for i in range(8, 20)]

# 模拟活动请求
activity_requests = [
    {'id': 1, 'type': '会议', 'scale': '小', 'duration': 1, 'preferred_time_slots': [(8, 9), (12, 13), (17, 18)]},
    {'id': 2, 'type': '研讨会', 'scale': '大', 'duration': 2, 'preferred_time_slots': [(9, 11), (13, 15), (16, 18)]},
    {'id': 4, 'type': '社交活动', 'scale': '小', 'duration': 2, 'preferred_time_slots': [(10, 12), (14, 16), (18, 20)]},
    {'id': 5, 'type': '会议', 'scale': '大', 'duration': 1, 'preferred_time_slots': [(9, 10), (12, 13), (16, 17)]},
    {'id': 7, 'type': '培训', 'scale': '小', 'duration': 2, 'preferred_time_slots': [(9, 11), (12, 14), (15, 17)]},
    {'id': 8, 'type': '社交活动', 'scale': '大', 'duration': 1, 'preferred_time_slots': [(10, 11), (13, 14), (18, 19)]},
    {'id': 10, 'type': '研讨会', 'scale': '小', 'duration': 1, 'preferred_time_slots': [(8, 9), (11, 12), (16, 17)]},
    {'id': 11, 'type': '培训', 'scale': '大', 'duration': 2, 'preferred_time_slots': [(10, 12), (14, 16), (17, 19)]},
    {'id': 13, 'type': '会议', 'scale': '小', 'duration': 1, 'preferred_time_slots': [(8, 9), (12, 13), (17, 18)]},
    {'id': 14, 'type': '研讨会', 'scale': '大', 'duration': 2, 'preferred_time_slots': [(9, 11), (13, 15), (16, 18)]},
    {'id': 16, 'type': '社交活动', 'scale': '小', 'duration': 2, 'preferred_time_slots': [(10, 12), (14, 16), (18, 20)]},
    {'id': 17, 'type': '会议', 'scale': '大', 'duration': 1, 'preferred_time_slots': [(9, 10), (12, 13), (16, 17)]},
    {'id': 18, 'type': '培训', 'scale': '小', 'duration': 2, 'preferred_time_slots': [(9, 11), (12, 14), (15, 17)]},
    {'id': 19, 'type': '研讨会', 'scale': '小', 'duration': 1, 'preferred_time_slots': [(8, 9), (11, 12), (16, 17)]},
    {'id': 20, 'type': '研讨会', 'scale': '小', 'duration': 1, 'preferred_time_slots': [(8, 9), (11, 12), (16, 17)]},
]


# 按照活动类型优先级排序
activity_requests.sort(key=lambda x: activity_priority[x['type']], reverse=True)

# 按规模分类活动请求
activities_by_scale = {'小': [], '中': [], '大': []}
for activity in activity_requests:
    activities_by_scale[activity['scale']].append(activity)

def optimize_activities(scale, activities):
    num_classes = venues_count[scale] # 资源数目
    num_activities = len(activities) # 该类型内活动数量
    num_time_slots = len(time_slots) # 该机制下每次安排时的可选时间段数量
    num_vars = num_activities * 3  # 每个活动有三个时间段选择

    # 目标函数：最大化分配的活动数
    c = np.ones(num_vars) * -1  # 转换为最小化问题

    # 约束条件
    A = []
    b = []

    # 时间段使用情况约束
    slot_usage = np.zeros((num_time_slots, num_vars))
    activity_indices = {i: [] for i in range(num_activities)}  # 记录每个活动对应的变量索引

    # 填充时间段使用和活动对应变量索引
    var_index = 0
    for i, activity in enumerate(activities):
        for time_slot in activity['preferred_time_slots']:
            start, end = time_slot
            for hour in range(start, end):
                slot_usage[hour - 8, var_index] = 1
            activity_indices[i].append(var_index)
            var_index += 1

    # 添加时间段使用约束
    for hour in range(num_time_slots):
        A.append(slot_usage[hour, :])
        b.append(num_classes)  # 每个时间段最多只能有一个活动

    # 每个活动只能选择一个时间段
    for indices in activity_indices.values():
        activity_constraint = np.zeros(num_vars)
        for idx in indices:
            activity_constraint[idx] = 1
        A.append(activity_constraint)
        b.append(1)

    A = np.array(A)
    b = np.array(b)

    # 解线性规划问题
    res = linprog(c, A_ub=A, b_ub=b, bounds=(0, 1), method='highs')

    # 解析结果
    assigned_activities = []
    unassigned_activities = []
    if res.success:
        for i in range(num_activities):
            allocated = False
            for var_idx in activity_indices[i]:
                if res.x[var_idx] > 0.5:
                    assigned_activities.append((activities[i]['id'], activities[i]['preferred_time_slots'][var_idx % 3]))
                    allocated = True
                    break
            if allocated == False:  
                unassigned_activities.append((activities[i]['id'], activities[i]['preferred_time_slots']))             
    return assigned_activities, unassigned_activities

# 分别处理每个规模的活动
successful_results = {}
unsuccessful_results = {}
for scale in ['小', '中', '大']:
    if activities_by_scale[scale] == []:
        continue
    successful_results[scale], unsuccessful_results[scale] = optimize_activities(scale, activities_by_scale[scale])
    
    
num_time_slots = len(time_slots) # 该机制下每次安排时的可选时间段数量
num_venue_type = len(venues_count)# 场地资源类型
usage_situation=np.zeros((num_time_slots,num_venue_type))
# 输出结果
for scale in successful_results:
    print("**************************************************************************")
    print(f"Successful Results for {scale} venues:")
    for res in successful_results[scale]:
        activity_id, time_slot = res
        venue_index = list(venues_count.keys()).index(scale)
        start,end=time_slot
        maxnum=0
        for starttime in range(start,end):
            slot_index = time_slots.index((starttime,starttime+1))
            usage_situation[slot_index][venue_index] += 1
            maxnum=max(maxnum,usage_situation[slot_index][venue_index])
        num=int(maxnum-1)
        print(f"Activity ID {activity_id} assigned to {venues_by_size[scale][num]} venue at time slot {time_slot}")

    print(f"Unsuccessful Results for {scale} venues:")
    for res in unsuccessful_results[scale]:
        activity_id, time_slot = res
        print(f"Activity ID {activity_id} unassigned from {scale} venue at time slot {time_slot}")

# Printing the usage_situation
print("\nUsage Situation:")
print(usage_situation)