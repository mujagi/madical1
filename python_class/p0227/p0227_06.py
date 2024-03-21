# 입력 : 이름, 아이디, 비밀번호 (input)
# 5명을 입력받아서 member 리스트를 만드세요

member = [ ] # [[홍길동, aaa, 111], [유관순, bbb,111]]
'''
member 리스트를
이름 아이디 비밀번호
홍길동 aaaa 1111
이순신 bbbb 2222

형식으로 출력해보세요
'''
for i in  range(5):
    name = input('이름을 입력해주세요>>>')
    id = input('아이디를 입력해주세요>>>')
    pw = int(input('비밀번호를 입력해주세요>>>'))
    m = [name,id,pw]
    member.append(m)
    
print('이름\t아이디\t비밀번호')
for i in range(len(member)) :
    print('{}\t{}\t{}'.format(member[i][0],member[i][1],member[i][2])) 
    # i는 위의 내가 지정한 그룹의 앞에 순번 매긴다
    # 맨 위 for문 range(5) = 다섯번 반복 member에 질문한 값이 순차적으로 저장 
    # 밑의  for문 range(len(member)) = 맨 위 for 문에 저장된 그룹의 길이만큼 반복 이라는 뜻
    # 저장된 그룹들 앞에 순차적으로 i가 번호를 매긴다 
    # member[0][0] = member[i][0] i는 순서대로 시작하기 때문에 가장 첫번째로 입력한 그룹

#print('{}\t{}\t{}'.format(member[0][0],member[0][1],member[0][2]))
#print('{}\t{}\t{}'.format(member[1][0],member[1][1],member[1][2]))
#print('{}\t{}\t{}'.format(member[2][0],member[2][1],member[2][2]))
#print('{}\t{}\t{}'.format(member[3][0],member[3][1],member[3][2]))
#print('{}\t{}\t{}'.format(member[4][0],member[4][1],member[4][2]))