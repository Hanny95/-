from urllib import request as rq
from urllib import parse as ps


# XML 데이터 로드
# rssURL = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184'

# rssURLData = rq.urlopen(rssURL).read()
# # 파일 디코딩
# rssText = rssURLData.decode('UTF-8')
# print(f'rssText : {rssText}')

# XML 데이터 로드(parse 이용)
rssURL = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
locationCode = {'stnId':'133'}
params = ps.urlencode(locationCode)
print(f'params : {params}')

rssURL = rssURL + '?' + params
print(f'rssURL : {rssURL}')

rssData = rq.urlopen(rssURL).read()
rssText = rssData.decode('UTF-8')
print(f'rssText : {rssText}')

# Q1 사용자가 지역(행정)코드를 입력하면, 해당 지역의 날씨 정보(RSS) 가 출력되는 모듈(함수, 클래스) 만들기
# Q2 Q1 을 해결한 후, 유효한 행정코드가 아닌 경우 '유효한 행정코드가 아닙니다! 다시 입력하세요' 출력하기

