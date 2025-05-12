import numpy as np
m=int(input("Nhập số lượng khu vực các điểm kinh tế: "))
print("Nhập khối lượng hàng của từng điểm(tấn): ")
supply=[]
for i in range(m):
    s=float(input())
    supply.append(s)
supply=np.array(supply)

n=int(input("Nhập số lượng điểm tiêu thụ hàng: "))
print("Nhập khối lượng nhu cầu của từng điểm(tấn): ")
domand=[]
for i in range(n):
    s=float(input())
    domand.append(s)
domand=np.array(domand)

cost=[]
for i in range(len(supply)):
    A=[]
    for j in range(len(domand)):
        s=float(input(f"Nhập chi phí vận chuyển từ điểm phát A{i+1} đến điểm thu B{j+1}: "))
        A.append(s)
    cost.append(A)
cost=np.array(cost)
#Kiểm tra xem đầu vào (khối lượng hàng) có bằng đầu ra (nhu cầu) hay không?
if np.sum(supply)-np.sum(domand)<0: #Nếu cung bé hơn cầu
    supply=np.hstack((supply ,np.sum(domand)-np.sum(supply))) #Tạo 1 điểm cung giả với số lượng bằng hiệu của cầu và cung
    cost=np.vstack((cost, [0]*len(domand))) # Số tiền vận chuyển là 0
elif np.sum(supply)-np.sum(domand)>0: #Nếu cung lớn hơn cầu
    domand=np.hstack((domand, np.sum(supply)-np.sum(domand))) #Tạo 1 điểm cầu giả với số lượng bằng hiệu của cung và cầu
    cost=np.hstack((cost, np.zeros((len(supply),1)))) #Số tiền vận chuyển là 0
allocation=np.zeros_like(cost) #Tạo một biến có kích thước của biến cost
s=supply.copy()
d=domand.copy()
while np.any(s > 0) and np.any(d > 0): #Kiểm tra xem còn phần tử nào trong s và d lớn hơn 0 hay không
    mask = np.outer(s > 0, d > 0) #Lấy mảng d nhân lần lượt cho mảng c; >0 được dùng để trả về toán tử bool
    
    if d.shape[0] > n: #Kiểm tra xem bài toán có biến giả hay không
        real_mask = mask[:, :n] #Nếu có, ngắt tạm thời vị trí có biến giả
        real_cost = np.where(real_mask, cost[:, :n], np.inf) #Nếu real_mask là true, real_cost được gán bằng cost, nếu không sẽ gán inf

        if np.any(real_mask): #Nếu vần còn phần tử true trong real_mask
            a, b = np.unravel_index(np.argmin(real_cost), real_cost.shape) #gán a là vị trí phần tử nhỏ nhất của real_cost, b là kích thước của real_cost
        else: #nếu không
            masked_cost = np.where(mask, cost, np.inf)#Lấy phần tử bao gồm cả biến giả
            a, b = np.unravel_index(np.argmin(masked_cost), masked_cost.shape)
    else:# Nếu không
        masked_cost = np.where(mask, cost, np.inf)
        a, b = np.unravel_index(np.argmin(masked_cost), masked_cost.shape)

    x = min(s[a], d[b]) 
    allocation[a][b] = x
    s[a] -= x
    d[b] -= x
result=np.sum(cost*allocation)
print(f"Bảng phân phối tối ưu: ")
for i in range(len(supply)):
    for j in range(len(domand)):
            print(f"A{i+1} -> B{j+1}: {allocation[i][j]} tấn và chi phí là {cost[i][j]}")
print(f"Chi phí vận chuyển nhỏ nhất là: {result}")