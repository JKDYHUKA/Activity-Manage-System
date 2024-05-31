from datetime import datetime, timedelta

def get_number(activity_level):
    if activity_level == '0-50':
        return 1
    elif activity_level == '50-100':
        return 2
    elif activity_level == '100-200':
        return 3
    else:
        return -1


def calculate_hours_difference_from_tomorrow_midnight(date_str):
    # 解析日期时间字符串为 datetime 对象
    date = datetime.fromisoformat(date_str.replace('Z', '+00:00'))

    # 获取当前时间
    now = datetime.utcnow()
    # 计算明天凌晨0点的时间
    tomorrow_midnight = datetime(now.year, now.month, now.day) + timedelta(days=1)
    tomorrow_midnight = tomorrow_midnight.replace(tzinfo=None)
    date = date.replace(tzinfo=None)

    # 计算时间差（以秒为单位）
    diff_in_seconds = (date - tomorrow_midnight).total_seconds()
    # 将时间差转换为小时
    diff_in_hours = diff_in_seconds / 3600
    return diff_in_hours + 8
