-- 어제, 오늘, 내일
select sysdate-1,sysdate,sysdate+1 from dual;
-- 오늘, 이달의 첫일, 이달의 마지막일
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;
-- 두 날짜간 일수, 두 날짜간 달 수
select round(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date),2) from employees;
-- trunc 일단위 버림
select trunc(kor,-1) kor, count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;
-- 퀴즈 hire_date 날짜에서 월만 출력하시오.
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') hire_date, count(to_char(hire_date,'mm'))from employees
group by to_char(hire_date,'mm')
order by hire_date;
-- 퀴즈 hire_date yyyy 년도, 년도별 인월 수를 출력하시오.
select to_char(hire_date,'yyyy') hire_date, count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;
-- 형변환 - number, charactermdate
-- number 사칙연산가능, 쉼표표시안됨, 원화표시안됨.
-- char 사칙연산(+,-) 안됨, 쉼표표시가능, 원화표시가능
-- date +,- 가능 / 날씨 출력형태는 변경불가
-- 시퀀스 평태로 학번을 부여하시오.
-- stu_seq 시퀀스를 가지고 5명의 학번을 출력해보세요
-- ko+2024+0001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;
-- (123,456,789)+(156,778) = ? 출력하시오.
-- (123,456,789)+(100,000) = 123556789 출력하시오.
select to_number(replace('123,456,789',',',''))+to_number(replace('156,778',',','')) from dual;
select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;
select to_char(salary,'$999,999') salary from employees;

--숫자타입을 날짜타입으로 변경
select 20240425+3 from dual; -- 숫자타입
select to_char(20240425+3) from dual; --문자타입
select to_date(20240425+3) from dual; --날짜타입

-- 숫자타입을 날짜타입으로 변경
select emp_name,hire_date from employees
where hire_date >to_date(20070101)
order by hire_date;

--퀴즈 01,02,08월 입사했으면서 이름 2번째에 a가 들어가있는 사람출력
select emp_name,hire_date from employees
where to_char(hire_date,'mm') in ('01','05','08') and emp_name like '_a%';

--퀴즈, 20070101 이후 입사한 사원이름 a가 들어가있는 사람을 출력하시오.
select emp_name,hire_date from employees
where hire_date>to_date(20070101) and emp_name like '%a%'
order by hire_date;

--문자타입을 날짜타입으로 변경
select sysdate - to_char('20240401') from dual;

select sysdate,'2024-04-01', sysdate-to_date('2024-04-01') from dual;

select *from m_date;



create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);

--입력시 날짜 타입에 문자(형태 = 날짜형태)를 입력해도저장
-- 날짜와 문자를 빼기는 불가능, 그래서 문자를 날짜타입으로 변경해야 함.
insert into eventDate values(
seq_mno.nextval,'2024-04-01',sysdate,sysdate-to_date('2024-04-01')
);

select *from eventDate;

--문자타입을 숫자타입으로 변경
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

--null을 0으로 치환 nvl()
select salary,commission_pct,salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

--숫자타입이 문자타입으로 변경
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;

--그룹함수 : count,sum,avg,min,max


-- 그룹함수 count(대상) = 총갯수
select count(emp_name) from employees;
select count(*) from employees; -- count(*) null값 포함 계산
select count(manager_id) from employees; --107개가 정상이지만 null 값이 포함이 안되서 106개로 출력
select emp_name,manager_id from employees;

-- sum : 총합
select sum(salary) from employees;
select to_char(sum(salary),'999,999') from  employees;

-- avg : 평균
select avg(salary) avg_sal from employees;

-- min : 최소값, max : 최대값
select min(salary), max(salary) from employees;

--퀴즈
--6461 달러보다높은 사람을 출력하시오
select emp_name,salary from employees
where salary> (select avg(salary) avg_sal from employees) 
order by salary;

-- 단일 함수, 그룹함수는 같이 사용이 안됨
select emp_name,min(salary) from employees;

--퀴즈최소월급을 받는 사람의 이름을 출력하시오
select employee_id,emp_name,salary from employees
where salary = (select min(salary) from employees);

- 퀴즈 최대월급 받는 사람의 사번, 이름 출력
select employee_id,emp_name,salary from employees
where salary = (select max(salary) from  employees);

-- 부선번호가 50번인 사원만 전체 합계
select department_id,salary from employees;

select sum(salary) from employees
where department_id = 50;

select count(*) from stu_score;

-- 퀴즈 kor점수가 80점 이상인 학생을 출력하시오
select name,kor from stu_score
where kor>=80 
order by kor;
-- 퀴즈, 국어점수에서 국어점수 평균이상, 영어점수 평균이상인 학생을 출력하시오
select name,kor,eng from stu_score
where kor>=(select avg(kor) from stu_score) and eng>=(select avg(eng) from stu_score);

create table s_info(
sno number,
s_count number
);

insert into s_info values(
seq_mno.nextval, (select count(*) from stu_score
where kor>=(select avg(kor) from stu_score) and eng>=(select avg(eng) from stu_score))
);

select *from s_info;

-- 퀴즈 월급 최대, 최소 출력, 평균인 사원 출력

select emp_name,salary from employees
where salary = (select max(salary) from employees) or 
salary = (select min(salary) from employees) or
salary = (select max(salary) from ( 
select emp_name,salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc));




--평균보다 낮은 값 중 가장 높은 값찾기
select max(salary) from ( 
select emp_name,salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc);

-- 문자함수
-- lpad
select emp_name,lpad(emp_name,15,'#') from employees; -- lpad: 왼쪽에 남는자릿수 만큼 '#' 채움
select emp_name,rpad(emp_name,20,'@') from employees; -- rpad: 오른족에 남는자릿수 만큼 '@' 채움

select emp_name,ltrim(emp_name,'Do')from employees; -- ltrim: emp_name 값 왼쪽의 'Do' 를 잘라줘

select 'ko20240001',ltrim('ko20240001','ko2024') from dual;

select emp_name, substr(emp_name,3,4) from employees; -- substr : (대상,순번,잘라올 갯수) 순번부터 시작해서 잘라올 갯수를 잘라온다

select job_id from employees;
select *from employees;
--퀴즈 job_id sh와 사원번호를 결합해서 출력하시오
select substr(job_id,1,2)||employee_id from employees; 

--length : 문자열의 길이
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

--날짜 함수
-- 날짜데이터 +,- 숫자 =가능
select sysdate+1 from dual;
-- 날짜데이터 - 날짜데이터 = 가능
select sysdate-hire_date from employees;
-- 날짜데이터 + 날짜데이터 = 불가능
select sysdate+hire_date from employees;

select sysdate,trunc(sysdate,'month'),round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

-- 개월수 추가,축소
select sysdate,add_months(sysdate,3) from dual;
select sysdate,add_months(sysdate,-2) from dual;

-- ceil : 올림, floor : 버림, mod : 나머지, power : 제곱
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;

--퀴즈  테이블에서 사원이름 입사일 
select *from employees;
select emp_name,hire_date from employees;

select emp_name,hire_date,emp_name||to_char(hire_date,' YYYY"년"MM"월"DD"일"') from employees;

-- 퀴즈, 사원명,자리수 9자리,빈공백 0으로 표시,월급*1400 앞에 원하표시와 쉼표를 넣어 출력하시오.
select emp_name,salary,to_char(salary*1400, 'L000,000,000') from employees;

-- 자신의 생일과 자신의 생일이 속한 달의 마지막 날짜
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;

select *from member;

desc member;

--colum 추가, 삭제, 수정
--commit,rollback이 안됨 바로 저장됨
alter table member add gender varchar2(6) default 'female' not null;

-- 컬럼삭제 commit, rollback 이 없음.
alter table member drop column phone;

-- 컬럼수정 : 컬럼이름, 타입변경
alter table member rename column name to stu_name; -- 이름변경
alter table member modify(stu_name varchar2(50));  -- 타입변경
alter table member modify(stu_name varchar2(3)); --기존의 문자열이 변경하려는 크기를 넘기 떄문에 변경 불가능, 작을경우는 가능
alter table member modify(stu_name number(100)); -- 다른 타입으로 변경하려는 경우 데이터를 빈공백 또는 null 로 변경 후 타입변경해야 가능

update member set gender = 'male' ;

commit;
