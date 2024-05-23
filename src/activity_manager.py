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

# 场地数量
venue_count = {
    '小': 3,
    '中': 2,
    '大': 1
}

# 有效时间区域（8点到20点）
time_slots = [(i, i+1) for i in range(8, 20)]

# 模拟活动请求
activity_requests = [
    {'id': 1, 'type': '会议', 'scale': '中', 'duration': 1, 'preferred_time_slots': [(8, 9), (12, 13), (17, 18)]},
    {'id': 2, 'type': '研讨会', 'scale': '中', 'duration': 2, 'preferred_time_slots': [(8, 9), (12, 13), (17, 18)]},
]


# 按照活动类型优先级排序
activity_requests.sort(key=lambda x: activity_priority[x['type']], reverse=True)

# 按规模分类活动请求
activities_by_scale = {'小': [], '中': [], '大': []}
for activity in activity_requests:
    activities_by_scale[activity['scale']].append(activity)

def optimize_activities(scale, activities):
    num_classes = venue_count[scale] # 资源数目
    num_activities = len(activities)
    num_time_slots = len(time_slots)
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

# 输出结果
for scale in successful_results:
    print("**************************************************************************")
    print(f"Successful Results for {scale} venues:")
    for res in successful_results[scale]:
        activity_id, time_slot = res
        print(f"Activity ID {activity_id} assigned to {scale} venue at time slot {time_slot}")
    print(f"Unsuccessful Results for {scale} venues:")
    for res in unsuccessful_results[scale]:
        activity_id, time_slot = res
        print(f"Activity ID {activity_id} unassigned from {scale} venue at time slot {time_slot}")
