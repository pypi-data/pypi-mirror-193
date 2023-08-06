import pytest

from freedom_utils import wmath


distance_test_case_list = [
    {
        "desc": "锐角",              # 点和线段连个端点的两个夹角的最大值为锐角
        "point": [1, 1],            # 点
        "line": [[1, 4], [5, 1]],   # 线段
        "pedal": [2.44, 2.92],      # 点到线段所在直线的垂足
        "distance": 2.4,            # 点到线段的最短距离
        "pedal_on_segment": True,   # 垂足是否在线段内
    },
    {
        "desc": "直角",
        "point": [1, 4],
        "line": [[1, 1], [5, 1]],
        "pedal": [1.0, 1.0],
        "distance": 3.0,
        "pedal_on_segment": True,
    },
    {
        "desc": "直角2",
        "point": [5, 1],
        "line": [[1, 1], [1, 4]],
        "pedal": [1, 1],
        "distance": 4.0,
        "pedal_on_segment": True,
    },
    {
        "desc": "钝角",
        "point": [1967.3095967910422, 7541.0424765635225],
        "line": [[1997.1667396481841, 6408.852000373047], [1997.1667396481841, 6363.852000373047]],
        "pedal": [1997.1667396481841, 7541.0424765635225],
        "distance": 1132.5840910749218,
        "pedal_on_segment": False,
    },
    {
        "desc": "平行y轴, 线段外",
        "point": [1, 1],
        "line": [[1, 8], [1, 9]],
        "pedal": [1, 1],
        "distance": 7.0,
        "pedal_on_segment": False,
    },
    {
        "desc": "平行x轴, 线段外",
        "point": [1, 1],
        "line": [[7, 1], [8, 1]],
        "pedal": [1.0, 1.0],
        "distance": 6.0,
        "pedal_on_segment": False,
    },
    {
        "desc": "平行x轴, 线段内",
        "point": [7, 1],
        "line": [[1, 1], [8, 1]],
        "pedal": [7.0, 1.0],
        "distance": 0.0,
        "pedal_on_segment": True,
    },
    {
        "desc": "平行x轴, 线段内",
        "point": [1, 7],
        "line": [[1, 1], [1, 8]],
        "pedal": [1, 7],
        "distance": 0.0,
        "pedal_on_segment": True,
    },
]


class TestWMath:

    def test_distance(self):

        for case in distance_test_case_list:
            print(case["desc"])
            p = wmath.pedal(case["point"], case["line"][0], case["line"][1])
            assert list(p) == case["pedal"]
            assert wmath.is_point_on_line_segment(p, case["line"]) == case["pedal_on_segment"]
            assert wmath.get_point_to_segment_nearest_distance(case["point"], case["line"]) == case["distance"]
