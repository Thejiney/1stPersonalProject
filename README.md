# 1차 프로젝트
> 개별 프로젝트

- 프로젝트명 : 김형진 (인원 1명)
- 기간 : 2024.01.13 ~ 2025.01.26(2주)
- 언어 : Python 3.10
- python openSource : https://github.com/shaked6540/YoutubePlaylistDownloader 
- python library : Librosa 0.10.2 Numpy 1.23.5 Pandas 1.5.3 Tensorflow 2.10.0 Matplotlib 3.7.0, Seaborn 0.12.2
- 마이크로 프레임워크 : FastAPI
- 프로젝트 소개 : 지역별 1인 가구 세대 및 매매가 평균 분석, 음악 재생목록 추천 AI

<div align=center> 
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/tensorflow-55ff55?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/sklearn-55ff55?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/fastapi-FF0000?style=for-the-badge&logo=fastapi&logoColor=white">
</div>
<div align=center> 
  <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
  <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
  <img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
</div>
<div align=center> 
  <img src="https://img.shields.io/badge/librosa-7952B3?style=for-the-badge&logo=librosa&logoColor=white">
  <img src="https://img.shields.io/badge/github-E34F26?style=for-the-badge&logo=github&logoColor=white"> 
</div>

## 목차
[1. 주제](https://github.com/Thejiney/1stPersonalProject?tab=readme-ov-file#1-%EC%A3%BC%EC%A0%9C)<br>
[2. 구현목표](https://github.com/Thejiney/1stPersonalProject?tab=readme-ov-file#2-%EA%B5%AC%ED%98%84%EB%AA%A9%ED%91%9C)<br>
[3. 전처리](https://github.com/Thejiney/1stPersonalProject?tab=readme-ov-file#3-%EC%A0%84%EC%B2%98%EB%A6%AC)<br>
[4. 시각화](https://github.com/Thejiney/1stPersonalProject?tab=readme-ov-file#4-%EC%8B%9C%EA%B0%81%ED%99%94)<br>
[5. 딥러닝 모델](https://github.com/Thejiney/1stPersonalProject?tab=readme-ov-file#5-%EB%94%A5%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8)<br>
[6. 웹구현](https://github.com/Thejiney/1stPersonalProject?tab=readme-ov-file#6-%EC%9B%B9%EA%B5%AC%ED%98%84)<br>

## 1. 주제
<img src="https://private-user-images.githubusercontent.com/179419272/406795077-46fcf7e8-f439-44f2-aaee-e06a3c4076db.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzc5NTAyNzEsIm5iZiI6MTczNzk0OTk3MSwicGF0aCI6Ii8xNzk0MTkyNzIvNDA2Nzk1MDc3LTQ2ZmNmN2U4LWY0MzktNDRmMi1hYWVlLWUwNmEzYzQwNzZkYi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEyN1QwMzUyNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YTVmNTJiM2U3ZWMwMDhmM2IxYzBmNjlkNWNlNGQzM2ZhN2RkZGE5ZDhiOGJlMDkyOWNjNTg4ZjNlZWMzMTJiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.wkp78QclLSZzxfrRe3cfkKSS-K833caS0EdLJ53oiUQ" alt="1첫대문">
![1첫대문](https://private-user-images.githubusercontent.com/179419272/406795077-46fcf7e8-f439-44f2-aaee-e06a3c4076db.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Mzc5NTAyNzEsIm5iZiI6MTczNzk0OTk3MSwicGF0aCI6Ii8xNzk0MTkyNzIvNDA2Nzk1MDc3LTQ2ZmNmN2U4LWY0MzktNDRmMi1hYWVlLWUwNmEzYzQwNzZkYi5QTkc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTI3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDEyN1QwMzUyNTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YTVmNTJiM2U3ZWMwMDhmM2IxYzBmNjlkNWNlNGQzM2ZhN2RkZGE5ZDhiOGJlMDkyOWNjNTg4ZjNlZWMzMTJiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.wkp78QclLSZzxfrRe3cfkKSS-K833caS0EdLJ53oiUQ)
## 2. 구현목표

## 3. 전처리

## 4. 시각화

## 5. 딥러닝 모델

## 6. 웹구현