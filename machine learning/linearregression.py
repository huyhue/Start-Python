import numpy as np  
#Import thư viện
import matplotlib.pyplot as plt
# A = np.loadtxt('univariate.txt', delimiter =',') #load univariate.txt to A
# print(A[0:4,:]) #print first 4 rows of A

# A = [ [ 1, 2 ], [ 3, 4 ] ] #create a 2*2 matrix
# np.savetxt('Saved_A.txt', A, fmt = '%.2f', delimiter = ',') #save A to Saved_A.txt

#import toàn bộ file univariate.txt
X = np.loadtxt('univariate.txt', delimiter = ',')
#import Theta từ file univariate_theta.txt
Theta = np.loadtxt('univariate_theta.txt')

#Lưu cột y
y = np.copy(X[:,-1])
#Chuyển cột đầu (x1) sang cột thứ 2
X[:,1] = X[:,0]
#Đổi cột đầu thành số 1
X[:,0] = 1
#Tính lợi nhuận (đơn vị 10000$)
predict = X @ Theta
#Chuyển lợi nhuận về đơn vị $
predict = 10000 * predict
#in cặp dân số-lợi nhuận đầu tiên (đơn vị dân số: người)
print('%d người : %.2f$' %(X[0,1]*10000,predict[0]))
#Lưu kết quả
np.savetxt('predicted_value.txt',predict,fmt = '%.6f')

#Plot giá trị thực tế (không lấy cột bias 1 đầu)
#X[:,1:] là x-axis của biểu đồ, không lấy cột đầu; y là y-axis, rx là red x, plot dữ liệu bằng dấu x màu đỏ
plt.plot(X[:,1:],y,'rx')
#Plot dự đoán
# plt.plot(X[:,1:],predict/10000,'-b')#ta dùng đơn vị gốc là 10000$, -b là đường thẳng màu xanh
#show kết quả
plt.show()