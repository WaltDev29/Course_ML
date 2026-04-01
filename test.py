
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cluster


# 테스트용 닥스훈트 데이터
test_dach_length = [76, 82, 79]
test_dach_height = [24, 27, 23]

# 테스트용 사모예드 데이터
test_samo_length = [84, 87, 81]
test_samo_height = [55, 58, 52]

# 합치기
test_length = np.array(test_dach_length + test_samo_length)
test_height = np.array(test_dach_height + test_samo_height)

# y 데이터 (테스트용 입력 데이터)
test_data = np.column_stack((test_length, test_height))


def model_predict_plot(model, x):
    labels = model.predict(x)
    colors = np.array(["red", "green", "blue", "magenta"])
    plt.scatter(x[:, 0], x[:, 1], c=colors[labels])
    plt.show()



import pickle
kmeans = None

with open("dog_model.pkl", "rb") as f:
    kmeans = pickle.load(f)

model_predict_plot(kmeans, test_data)