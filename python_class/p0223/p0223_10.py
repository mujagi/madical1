#해보세요
#성별, 키를 입력받아서
#남자일 경우 (m) 172.5이상이면[평균이상] 이하면 [평균이하]
#여자일 경우 (f) 159.6이상이면 [평균이상] 이하면 [평균이하]
#라고 출력해보세요
gender = input('성별을 입력하세요(m/f)>>')
height = float(input('키를 입력해주세요>>'))
if gender=='m' :
    if height >= 172.6:
        print('평균이상')
    else :
        print('평균이하')
elif gender=='f':
    if height >= 159.6 :
        print('평균이상')
    else :
        print('평균이하')
else :
    print('잘 못 입력하셨습니다.')