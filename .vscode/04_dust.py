import requests
from bs4 import BeautifulSoup

KEY = 'AIiP14yZQkZ7gURpstTASJFBtokqG8l3u5lJDAmhTS6s6XnhlEzO3Q34J%2FCX0Zu5fVsAtL1nKrSFqlA0067OuQ%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=AIiP14yZQkZ7gURpstTASJFBtokqG8l3u5lJDAmhTS6s6XnhlEzO3Q34J%2FCX0Zu5fVsAtL1nKrSFqlA0067OuQ%3D%3D&numOfRows=10&pageNo=3&sidoName=서울&ver=1.0'
# print(url)
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[7]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')

if dust > 150:
    print('매우나쁨')
elif 80 < dust and dust <= 150: #dust > 80
#파이썬만가능함 어디에서 어디까지
    print('나쁨')
elif 30 < dust and dust <= 80: #dust >30
    print('보통')
else:
    print('좋음')