from Download import downloadData as dld

url = 'https://ssl.pstatic.net/tveta/libs/1353/1353461/923fd98ff636450628b6_20211013015401831_2.jpg'
path = 'C:/chh_scraping/download/img/'
fileName = 'New.jpg'

# result = dld.downloadDataAtNetwork(url, path, fileName)
#
# if result == 1:
#     print('success')
#
# else:
#     print('fail')

#-----------------------------------------------------------------#
## 클래스 > 객체 생성
ddan = dld.DownloadDataAtNetwork(url, path, fileName)
result = ddan.downloadData()

# if result == 1:
#     print('success!')
#
# else:
#     print('fail!')

# 경로바꿈
ddan.setUrl('https://ssl.pstatic.net/tveta/libs/1353/1353461/e283178e35404a4a5134_20211013020131452_2.jpg')
ddan.setFileName('myNewImg.jpg')
ddan.downloadData()