#ctrl +shipf + F10 : 실행
# 패키지(모듈) 불러오기 (웹 상 작업 > urllib 패키지 사용)
from urllib import request as rq

# 이미지 주소 / 저장할 경로 / 이미지 이름
url = 'https://ssl.pstatic.net/tveta/libs/1338/1338324/1c5eaa4100898ecf1faf_20211012150009401.jpg'
path = 'C:/chh_scraping/download/img/'
fileName = 'myBannerImg.jpg'

# request.urlretrieve (매개변수 2개받음) : 데이터 다운로드
# 시스템이 아웃되지 않도록 예외처리해주는것이 좋음
try:
    rq.urlretrieve(url, path + fileName)
except Exception as e:
    print(e)
    print('image download fail!')
# else & finally 생략가능
else:
    print('image download success!')
finally:
    print('image download complete!')


# ------------------------------------------------------------------- #
# request.urlopen : 데이터 (메모리상에) 로드
downloadInMemory = rq.urlopen(url).read()
print(f'downloadInMemory : {downloadInMemory}')

# wb > 텍스트파일이 아닌 이미지 파일이어서

try:
    with open(path + fileName, 'wb') as f:
        f.write(downloadInMemory)
except Exception as e:
    print(e)
else:
    print('image download success!')
finally:
    print('image download process complete!')

# 텍스트 파일 읽기 & 쓰기
# step01 : f = open('c:/tempDir/temp.txt', 'r')
# step02 : read() & write() -> str = f.read()
# step03 : close() -> f.close()  ** with as : close 생략 가능


# example
#  01 - urlretrieve() 를 이용해서 데이터 다운로드 하는 모듈(함수, 클래스)을 만들기
#  02 - urlopen() 를 이용해서 데이터 다운로드 하는 모듈(함수, 클래스)을 만들기 : 기능 2개 (다운로드만 할지 & 읽고쓸지)

