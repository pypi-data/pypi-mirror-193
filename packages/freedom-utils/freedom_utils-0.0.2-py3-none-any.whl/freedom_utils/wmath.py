import numpy as np


def pedal(p0, p1, p2):
    """
    过p0作p1和p2相连直线的垂线, 计算垂足的坐标
    直线1：垂足坐标和p0连线
    直线2: p1和p2连线
    两条直线垂直, 且交点为垂足

    Args:
        p0: (x0, y0)
        p1: (x1, y1)
        p2: (x2, y2)

    Returns: 垂足坐标 (x, y)

    """
    if p2[0] != p1[0]:
        # ########## 根据点x1和x2计算线性方程的k, b
        k, b = np.linalg.solve([[p1[0], 1], [p2[0], 1]], [p1[1], p2[1]])  # 得到k和b
        # print(k, b)
        # #######原理: 垂直向量数量积为0
        x = np.divide(((p2[0] - p1[0]) * p0[0] + (p2[1] - p1[1]) * p0[1] - b * (p2[1] - p1[1])),
                      (p2[0] - p1[0] + k * (p2[1] - p1[1])))
        y = k * x + b

    else:  # 点p1和p2的连线垂直于x轴时
        x = p1[0]
        y = p0[1]

    return x, y


def is_point_on_line_segment(point, line_segment):
    """
    判断点是否在线段上

    Args:
        point:
        line_segment:

    Returns:

    """
    p = np.array(point)
    p1 = np.array(line_segment[0])
    p2 = np.array(line_segment[1])

    # 求点到线段两个端点的距离
    p1_p2_distance = np.linalg.norm(p1 - p2)
    p_p1_distance = np.linalg.norm(p - p1)
    p_p2_distance = np.linalg.norm(p - p2)

    # 如果点到线段两个端点的距离和 等于 线段的长度, 证明点在线段上
    return p_p1_distance + p_p2_distance == p1_p2_distance


def get_point_to_segment_nearest_distance(point, line_segment):
    """
    求点到线段的最短距离

    Args:
        point:
        line_segment:

    Returns:

    """
    p0 = np.array(point)

    # 获取垂足坐标
    p1 = line_segment[0]
    p2 = line_segment[1]
    pedal_point = pedal(p0, p1, p2)
    print("垂足", pedal_point)

    if is_point_on_line_segment(pedal_point, line_segment):
        # 垂足在线段上, 点到线段的最短距离 为 点和垂足之间的距离
        return np.linalg.norm(p0 - pedal_point)
    else:
        # 垂足没在线段上, 点到线段的最段距离 为 到线段两个端点距离的较小者
        return min(np.linalg.norm(p0 - p1), np.linalg.norm(p0 - p2))
