N = int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)
#이어줄 때 ,를 사용해서 문제가 발생했다. 
# +를 사용해야했다 하지만 ,를 쓸때도 문제는 생기지 않았었다.
#지금보니까 ,로 연결하면 원치않는 공백 하나가 생긴다.