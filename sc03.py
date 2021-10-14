from Download import loadData as ld

url = 'https://ssl.pstatic.net/tveta/libs/1353/1353461/e283178e35404a4a5134_20211013020131452_2.jpg'

# 함수 불러오기
result = ld.loadDataInMemory(url)

if result == 1:
    print('success!')

else:
    print('fail')


#====================================
# 클래스 불러오기

load = ld.LoadDataInMemory(url)
result = load.loadData()

if result == 1:
    print('success!')

else:
    print('fail')


