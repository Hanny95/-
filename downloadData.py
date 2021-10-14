from urllib import request as rq

# 함수
def downloadDataAtNetwork(url, path, fileName):

    result = 0

    try:
        rq.urlretrieve(url, path + fileName)

    except Exception as e:
        print(e)
        print('[downloadData] [downloadDataAtNetwork()] download fail')
        result = 0

    else:
        print('[downloadData] [downloadDataAtNetwork()] download success')
        result = 1

    finally:
        print('[downloadData] [downloadDataAtNetwork()] Done')

    return result


# 클래스(속성 + 기능)
class DownloadDataAtNetwork:

    # 객체 생성함에 따라 속성 초기화시킴
    def __init__(self, u, p, f):
        self.url = u
        self.path = p
        self.fileName = f

    # 기능 구현
    def downloadData(self):

        result = 0

        try:
            rq.urlretrieve(self.url, self.path + self.fileName)

        except Exception as e:
            print(e)
            print('[downloadData] [DownloadDataAtNetwork] download fail')
            result = 0

        else:
            print('[downloadData] [DownloadDataAtNetwork] download success')
            result = 1

        finally:
             print('[downloadData] [DownloadDataAtNetwork] Done')

        return result


    # getter & setter 만들기

    def setUrl(self, u):
        self.url = u

    def setPath(self, p):
        self.path = p

    def setFileName(self, f):
        self.fileName = f

    def getUrl(self):
        return self.url

    def getPath(self):
        return self.path

    def getFileName(self):
        return self.fileName

    # 자바의 toString
    def printAttributeInfo(self):
        print(f'url:{self.getUrl()}')
        print(f'path:{self.getPath()}')
        print(f'fileName:{self.getFileName()}')





# if __name__ == '__main__':
#     url='https://ssl.pstatic.net/tveta/libs/1358/1358440/f8558e92c6c55230cc93_20211012141902904.jpg'
#     path='C:/chh_scraping/download/img/'
#     fileName='newFile.jpg'
#     result = downloadDataAtNetwork(url, path, fileName)
#
#     if result == 1:
#         print('success!')
#
#     else:
#         print('Fail!')