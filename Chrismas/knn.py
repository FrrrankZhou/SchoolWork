def e_distance(v1, v2):  # 计算欧几里得距离的函数
    return sum((v1[i] - v2[i]) ** 2 for i in range(len(v1))) ** 0.5


def insertion(given_list):  # 插入排序的函数
    for i in range(1, len(given_list)):
        for j in range(i, 0, -1):
            if given_list[j - 1] > given_list[j]:
                given_list[j], given_list[j - 1] = given_list[j - 1], given_list[j]
    return given_list


class KNN:
    def __init__(self, k, X, Y):  # k 是 k个最近的邻居，X 是训练集的数据，Y是训练集的类别
        self.k = k
        self.X = X
        self.Y = Y

    def prediction(self, test_x):  # 预测单个数据
        difference_list, nn = [], []  # 初始化两个列表
        # 倒序遍历每个训练集的数据
        for i in range(len(self.X), 0, -1):
            distance = e_distance(test_x, self.X[i - 1])  # 计算数据与每个训练集中的数据的欧几里得距离
            difference_list.append([distance, self.Y[i - 1]])  # 将给定数据与每个训练集的数据之间的距离和对应数据的类别存入该列表
        # 使用二分插入算法将上一步计算出的列表按照距离升序排列
        n = len(self.X)
        left_list, right_list = difference_list[0: (n // 2)], difference_list[(n // 2): n]  # 将刚才的总列表分成两半
        left, right = insertion(left_list), insertion(right_list)  # 对拆分出来的两个小列表分别使用插入排序算法
        difference_list = []  # 清空被拆半的总列表
        while (0 < len(left)) and (0 < len(right)):  # 合并两个小列表
            if right[0] > left[0]:
                difference_list.append(left.pop(0))
            else:
                difference_list.append(right.pop(0))
        if len(left) == 0:
            difference_list.extend(right)
        else:
            difference_list.extend(left)
        for n in range(self.k):  # 将最接近给定数据的前k个数据的类别存入列表“nn”
            nn.append(difference_list[n][1])
        y_predict = max(nn, key=nn.count)  # 使用少数服从多数原理预测给定数据的类别
        return y_predict

    def poly_prediction(self, test_X):  # 预测多个数据
        return [self.prediction(test_X[i])for i in range(len(test_X))]
