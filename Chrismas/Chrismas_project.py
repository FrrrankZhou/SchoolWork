from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pickle
import knn
from datetime import datetime
start = datetime.now()
digits = datasets.load_digits()  # 调用数据
labels, images = digits.target, digits.images  # 导入数据
# images[images > 8] = 255  # 二值化数据
samples, length, width = images.shape  # 存入数据的shape
data = images.reshape(samples, length * width)  # 将数据转为向量
total = 0
for counter in range(1, 4):  # 执行3次并取平均
    X_train, X_test, Y_train, Y_test = train_test_split(data, labels, test_size=0.2)  # 将数据按8：2分为训练集和测试集
    model = knn.KNN(1, X_train, Y_train)  # 实例化knn
    y_predict = model.polyprediction(X_test)  # 使用polyprediction方法预测测试集的类别
    matrix = confusion_matrix(Y_test, y_predict)  # 计算混淆矩阵
    print(matrix)  # 打印混淆矩阵
    rights = sum(matrix[i, i] for i in range(len(matrix)))  # 计算预测正确的数量
    accuracy = rights / len(Y_test)  # 计算正确率
    total += accuracy  # 加和每个正确率
print(total / counter)  # 计算并打印平均正确率

with open("model.db", "wb") as f:  # 打开文件“model.db”
    pickle.dump(model, f)  # 持久化对象
end = datetime.now()
print(end-start)
