select *from studeants;
-- 순차정렬
select *from students
order by name asc;
--테이블 컬럼추가
alter table students add rank number(3);

select * from students;

update students set rank=0;

select *from students;

select rank() over(order by total desc) rank
from students;

update  students set total=0;

select *from students;

update students set total =(kor+eng+math);


--1. update 구문
update students set rank = (rank);

--2 no,rank() 구문
(select no,rank() over(order by total desc) ranks from students) b;

--3. update구문과 rank() 구문을 no 컬럼으로 비교, rank컬럼을 검색
update student a set rank = (
select ranks from (students)b
where a.no = b.no
);

--4. students 테이블에서 ranks가 들어가 있는 테이블을 넣어줌
update students a set rank = (
select ranks from (select no,rank() over(order by total desc) ranks from students)
b where a.no = b.no
);

--역순 정렬
select no,total,rank from students
order by total desc;

--no 순차정렬
select no,total,rank from students
order by no;

select no,kor,eng,math,total,rank from students
order by kor desc, eng asc;

select manager_id from employees
order by  manager_id desc;

select max(hire_date)-min(hire_date) from employees
order by hire_date desc;

select max(kor)-min(kor) from students;
select max(kor),max(eng),max(math) from students;

-- 퀴즈
--입사일 오름차순 , 컬럼은 사원번호, 사원명, job_id = 직급, 입사일 월급 컬럼을 출력하시오.

select *from employees;

select employee_id,emp_name,job_id,hire_date,salary from employees
order by hire_date desc;

--퀴즈2
--급여를 적게 받는 순으로 출력하되월급이 같으면,사원명으로 순차정렬하시오
select salary,emp_name from employees
order by salary,emp_name desc;


--숫자함수
-- abs
select -10,abs(-10) from dual;
--floor : 소숫점 버림, round 소숫점 반올림  as 뭐시기 : 별칭
select 34.789, floor(34.789) as f,round(34.789) as r from dual;
--round(대상,자릿수) ex) round(34.178,2) 2자리까지 표시
select 34.178, round(34.178),round(34.178,2) from dual;

select avg from students;
select round(avg,2) avg from students;

select 34.5678, round(34.5678,-1) from dual;

-- trunc 지정한 자리수 이하 버림
select trunc(34.5678,2) from dual;

select trunc(34.5678,-1) from dual;

select trunc(34.5678) from dual;

--ceil : 올림, 자릿수가 없다
select ceil(34.123) from dual;

-- 국어점수 일단위 절삭해서 출력하시오,

select trunc(kor,-1) from students
order by kor;

-- 국어, 영어, 수학 점수를 일단위  절삭해서 합을 출력하시오.

select trunc(kor,-1) k, trunc(eng,-1) e, trunc(math,-1),(trunc(kor,-1)+trunc(eng,-1)+trunc(math,-1)) total from students;

--mod 나머지 계산
select round(100/7,2) from dual;
select mod(10,7) from dual;
--나누기
select 10/7 from dual;

-- 퀴즈, 사원번호가 짝수 인것을 출력하시오
-- 파이썬 employee_id%2=0
select employee_id from employees
where mod(employee_id,2)=0 ;

--몫
select floor(10/7) from dual;
--나머지 나머지가 0이면 짝수, 1이면 홀수
select mod(10,7) from dual;

-- 퀴즈 학생 학번이 3의 배수인것만 출력하시오
select no from students
where mod(no,3)=0;

--시퀀스
create sequence seq_no
increment by 1 --증감  1씩 됨
start with 1 -- 시작이 1부터  진행
minvalue 1 -- 최소값 1
maxvalue 9999 -- 최대값 9999
nocycle -- 순화하지 않음
nocache; -- 캐시 사용하지 않음

-- nextval 시퀀스 번호 1씩 증가
select seq_no.nextval from dual;

--currval 시쿼늣 번호 확인
select seq_no.currval from dual;

--drop table member;
--drop table mem;

create table member(
mno number(4),
id varchar2(30),
pw varchar2(20),
name varchar2(30),
phone varchar2(15)
);

create sequence seq_mno
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

select seq_mno.nextval from dual;

insert into member values (
seq_mno.nextval,'eee','1111','김구','010-5555-5555'
);

select *from member;




select sysdate  from dual;
select to_char(sysdate,'yyyy') from dual;

--'00000' 자리수
select 's'||to_char(seq_mno.nextval,'00000') from dual;


--퀴즈
---- 한국대학교 ko202400001
--시퀀스 seq_ko 1 - 99999
create sequence seq_ko
increment by 1
start with 1
minvalue 1
maxvalue 99999
nocycle
nocache;

--trim() 공백제거
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_ko.nextval,'00000')) as stuno from dual;

-- 게시판
create table board(
bno number(5) primary key,
btitle varchar2(1000),
bcontent varchar(3000),
id varchar2(30),
bdate date,
bhit number(10)
);


--퀴즈
--시퀀스 시작 1001 증감 10 최소값 1 최대 99999
-- 5번 실행을 해보세요

create sequence seq_deptno
increment by 10
start with 1001
minvalue 1
maxvalue 99999
nocycle
nocache;

select seq_deptno.nextval from dual;

create table emp01(
empno number(4) primary key,
ename varchar(30),
hire_date date
);

create sequence emp_seq
increment by 1
start with 1
minvalue 1
maxvalue 999
nocycle
nocache;

alter sequence emp_seq
increment by 1001
maxvalue 9999;

insert into emp01 values(
emp_seq.nextval,'유관순',sysdate
);

select *from emp01;

commit;

select *from employees;

--현재까지 입사한 일수를 함께 출력하시오. 소수점 올림

select employee_id,emp_name,job_id,hire_date,ceil(sysdate-hire_date)||'일'
from employees
order by hire_date desc;

select emp_name from employees;

--퀴즈
--직급과 사번을 합쳐서 출력하시오

select job_id||employee_id from employees;

-- 문자열자르기 함수 , substr(대상,시작위치,개수)
select substr(job_id,0,2) from employees;

select emp_name,substr(emp_name,1,3) from employees;

select substr('abcde',2,3) from dual;

--퀴즈
--job_id 앞에 2개 문자와 사번 5자리 00101를 만들어서 출력하시오

select substr(job_id,1,2)||to_char(employee_id,'00000') from employees;

--날짜 함수
select sysdate from dual;

select to_char(sysdate,'yyyy-mm-dd hh24:mi:ss') from dual;

--months_between : 몇개월 sysdate-hire_date : 몇일
select MONTHS_BETWEEN(SYSDATE,hire_date),sysdate-hire_date from employees;

-- 개월수를 추가
select sysdate,add_months(sysdate,2) from dual;

--next_day(입력,다음번 요일) 입력한 기준으로 다음번 요일을 알려줌
select next_day(sysdate,'월요일') from dual;

--입력한 기준으로 마지막일을 알려줌
select last_day(sysdate) from dual;

select last_day('2024-02-01') from dual;
