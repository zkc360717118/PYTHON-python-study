from sklearn import svm,datasets
import numpy as np

class Dataset:
    def __init__(self,name):
        self.name = name

    # 下载数据集
    def download_data(self):

        if self.name == "iris":
            #使用sklearn自带的数据集下载方法
            self.downloaded_data = datasets.load_iris()
        elif self.name == "digits":
            self.downloaded_data = datasets.load_digits()
        else:
            print('Dataset Error: No named datasets')

    #生成xy
    def generate_xy(self):
        # 通过这个过程来把我们的数据集分为原始数据以及他们的label
        # 我们先把数据下载下来
        self.download_data()
        x = self.downloaded_data.data
        y = self.downloaded_data.target
        print('\nOriginal data looks like this: \n', x)
        print('\nLabels looks like this: \n', y)
        return x, y

    def get_train_test_set(self, ratio):
        # 这里，我们把所有的数据分成训练集和测试集
        # 一个参数要求我们告知，我们以多少的比例来分割训练和测试集
        # 首先，我们把XY给generate出来：
        x, y = self.generate_xy()
        # 有个比例，我们首先得知道 一共有多少的数据
        n_samples = len(x)
        # 于是我们知道，有多少应该是训练集，多少应该是测试集
        n_train = int(n_samples * ratio)
        # 好了，接下来我们分割数据
        X_train = x[:n_train]
        y_train = y[:n_train]
        X_test = x[n_train:]
        y_test = y[n_train:]
        # 好，我们得到了所有想要的玩意儿
        return X_train, y_train, X_test, y_test  # ====== 我们的dataset类创造完毕=======

# 比如，我们使用digits数据集
data = Dataset('digits')
# 接着，我们可以用0.7的分割率把xy给分割出来
X_train, y_train, X_test, y_test = data.get_train_test_set(0.7)
#引用第三方类中的分类器
clf = svm.SVC()
#开始训练
clf.fit(X_train, y_train)

#开始在测试集中取一个数据
test_point = X_test[12]
# print(type(test_point)) # <class 'numpy.ndarray'>
# print(test_point) # 一维数组

#预测
test_point = np.array(test_point).reshape(1,-1)
# print(test_point)  #转换成2维数组了
pred_result =clf.predict(test_point)
print(pred_result)  # 7

#实际的结果
print(y_test[12])  #7