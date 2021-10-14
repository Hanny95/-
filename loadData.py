from urllib import request as rq

# 함수 만들기

def loadDataInMemory(url):

    result = 0

    try:
        rq.urlopen(url)

    except Exception as e:
        print(e)
        print('[loadData] loadDataInMemory() FAIL!')
        result = 0

    else:
        print('[loadData] loadDataInMemory() SUCCESS!')
        result = 1

    finally:
        print('[loadData] loadDataInMemory() DONE!')


    return result


# 클래스 만들기

class LoadDataInMemory:

    # 속성
    def __init__(self, url):
        self.url = url

    # 기능
    def loadData(self):

        result = 0

        try:
            rq.urlopen(self.url)

        except Exception as e:
            print(e)
            print('[loadData] [LoadDataInMemory] FAIL!')
            result = 0

        else:
            print('[loadData] [LoadDataInMemory] SUCCESS!')
            result = 1

        finally:
            print('[loadData] [LoadDataInMemory] DONE!')

        return result

    # getter & setter

    

