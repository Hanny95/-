from urllib import request as rq
from urllib import parse as ps

# 함수 만들기

def weatherRSSReader():

    url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

    while True:
        localCode = input('Please Input local code :')
        result = availableLocationCode(localCode)

        if result == 1:
            print('available code')

            locationCodeDic = {'stnId':localCode}
            params = ps.urlencode(locationCodeDic)

            url = url + '?' + params

            rssData = rq.urlopen(url).read()
            rssText = rssData.decode('UTF-8')

            print(f'rssText : {rssText}')

            break

        else:
            print('not avilable code')




def availableLocationCode(code):

    codes = {
        '108':'전국',
        '109':'서울,경기',
        '105':'강원도',
        '131':'충청북도',
        '133':'충청남도',
        '146':'전라북도',
        '156':'전라남도',
        '143':'경상북도',
        '159':'경상남도',
        '184':'제주도'
    }

    result = 0

    if code in codes:
        print('available code')
        result = 1
    else:
        print('not avilable code')
        result = 0

    return  result



# 클래스 만들기

class WeatherRSSReader:

    def __init__(self, lc = '108'):
        self.url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
        self.locationCode = lc

    def printWeatherRSS(self):

        while True:
            inputCode = input('Please input local code')
            result = availableLocationCode(inputCode)

            if result == 1:
                print('available')
                self.setLocationCode(inputCode)
                locationDic = {'stnId': self.locationCode}
                params = ps.urlencode(locationDic)
                rssURL = self.url + '?' + params

                rssData = rq.urlopen(rssURL).read()
                rssText = rssData.decode('UTF-8')

                print(rssText)

                break

            else:
                print('not available')



    def setLocationCode(self, lc):
        self.locationCode = lc

    def getLocationCode(self):
        return self.locationCode


if __name__ == '__main__':
    availableLocationCode(108)


    # try:
    #     localCode = input('지역 코드를 입력하세요')
    #     localCodeData = ps.urlencode(localCode)
    #     rssURL =  rssURL + '?stnId=' + localCodeData
    #
    #     rssData = rq.urlopen(rssURL).read()
    #     rssText = rssData.decode('UTF-8')
    #
    # except Exception as e:
    #     print(e)
    #     print('weatherInfo() fail')
    #
    # else:
    #     print('weatherInfo() success')
    #
    # finally:
    #     print('weatherInfo() Done')
    #
    #
    # return rssText


# 클래스 만들기