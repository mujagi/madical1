select * from stu_score;

select * from stu_score
where name like '_a%'
order by no asc;

select a.*, name from board a,member b
where a.id = b.id;

select bno, a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile
from board a,member b
where a.id = b.id;

select * from stu_score;

select no,name,total,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score
order by grade
;
select round(avg(salary),2) as salary from employees;
select * from employees;
-- employees 테이블에서 사원번호, 이름, 월급, 실제월급(월급+(월급*커미션)), 월급 *1410(원)원화로 환산해서
-- 원화표시, 천단위 표시해서 출력
select employee_id, emp_name,salary,salary+(salary*nvl(commission_pct,0)) real_salary,
to_char(salary*1410,'L99,999,999') kor_salary
from employees
order by employee_id;

select department_id,round(avg(salary),2),min(salary),max(salary) from employees
where department_id is not null
group by department_id
order by department_id;

-- 홍 이라고 검색하면 홍에 관련된 학생 모두 검색
select * from stu_score
where name like '%홍%'
order by no asc;
select name, avg from stu_score
where avg >= 60
order by no;

-- 사원번호, 사원명, 부서번호, 부서명을 출력하시오.
select employee_id, emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary >= (select avg(salary) from employees);

-- 그리고, 두번째 자리에 a가 들어가는 사원을 검색하시오.
select emp_name from employees
where emp_name like '_a%';

-- 월급이 평균이상인 사람만 검색하시오.
select salary from employees
where salary >= (select avg(salary) from employees);
select * from employees;
select * from departments;
select * from jobs;

-- 사원번호 e, 사원명 e, 부서번호 e, 부서명 d, 직급번호 e, 직급명 출력하시오
select e.employee_id, e.emp_name, e.department_id, d.department_name, j.job_id, j.job_title
from employees e, departments d, jobs j
where j.job_id =  e.job_id and e.department_id= d.department_id;

-- 사원번호, 사원명, 월급, 최소월급분,직급, 직급
select employee_id,emp_name,salary,min_salary,round(((salary-min_salary)/salary)*100,2),a.job_id,job_title
from employees a, jobs b
where a.job_id = b.job_id
;

-- job_title Manager 글자가 들어가 있는
-- 사원번호 e, 사원명 e, 직급번호 e, 직급명 j, 월급 e, 최대월급 j을 출력하시오
select *from jobs;
select *from employees;

select employee_id, emp_name, e.job_id, job_title, salary, max_salary from employees e, jobs j
where e.job_id = j.job_id and job_title like '%Manager%';

select a.user_id, user_name, user_phone,user_address1,user_address2,
user_address3
from User a, Deliver_address b
where a.user_id = b.user_id;

create table stu_grade(
grade varchar2(1) primary key,
low_score number(3) not null,
high_score number(3) not null
); 

insert into stu_grade values(
'A',90,100
);
insert into stu_grade values(
'B',80,89
);
insert into stu_grade values(
'C',70,79
);
insert into stu_grade values(
'D',60,69
);
insert into stu_grade values(
'F',0,59
);

commit;

select *from stu_grade;

select avg from stu_score;

--case when then 사용해서  90점 이상 A, B...... 학점 출력

select name,avg,
case
when avg>=90 then 'A'
when avg>=80 then 'B'
when avg>=70 then 'C'
when avg>=60 then 'D'
else  'F'
end as grade
from stu_score
order by grade
;

--non-equi join
select no,name,avg,grade
from stu_score,stu_grade
where avg between low_score and high_score
order by no
;

-- stu_score, stu_grade 같은 컬럼이 없음.
-- 2개 테이블을 join : non-equi join
select *from stu_score;
select *from stu_grade;

update stu_grade set low_score = 92
where grade = 'A'
;

update stu_grade set low_score = 82, high_score = 91
where grade = 'B'
;

update stu_grade set low_score = 72, high_score = 81
where grade = 'C'
;

update stu_grade set low_score = 62, high_score = 71
where grade = 'D'
;

update stu_grade set low_score = 0, high_score = 61
where grade = 'F'
;

-- 월별매출액을 기준으로 고객등급
-- 지역별 대출 합계
select *from kor_loan_status;
select region,gubun,sum(loan_jan_amt) j from kor_loan_status
group by region,gubun
order by region
;

-- 년도별, 지역별 대출 합계 금액
select substr(period,1,4),region,sum(loan_jan_amt) from kor_loan_status
group by substr(period,1,4),region
order by region
;



-- 부서별 월급 합계를 출력하시오.
select department_id,sum(salary) a from employees
group by department_id
order by a
;

-- 시간대별,연령대별 판매량 총합을 출력하시오
select *from lotte_product;

select time_cd,age_cd,sum(purh_amt) a from lotte_product
group by time_cd,age_cd
order by a desc
;

--2024/03/01 이후 이름별, 금액합계를 출력하시오
select *from shop_product;

select name, sum(amount) from shop_product
where p_date >= '2024/03/01'
group by name
;

-- customer_rank 테이블 생성
-- rank 
-- 100만원 미만 bronze
-- 200만원 미만 silver
-- 300만원 미만 gold
-- 300만원 이상 platinum

-- name,sum(amount), rank 출력하시오.
create table customer_rank(
grade varchar2(30) primary key,
low_num number(7) not null,
high_num number(7) not null
);

insert into customer_rank values(
'platinum',3000000,9999999);

select *from customer_rank;
select *from shop_product;

select name,s_amount,grade
from
(select name,sum(amount) s_amount 
from shop_product
where p_date>='2024/03/01'
group by name
),customer_rank
where s_amount between low_num and high_num 
;

select *from lotte_product
order by std_ym ;

-- 순번을 새롭게 부여해서 출력해주는 함수
-- row_num, row_number()
select rownum,std_ym,sex_cd,age_cd,purh_amt
from lotte_product;

select rownum,a.* from lotte_product a
where rownum<=10 ;
from lotte_product a;

select rnum,std_ym,sex_cd,age_cd,time_cd,purh_amt
from 
(
select rownum rnum,a.* from lotte_product a
) b
where rnum >=11 and rnum<=20;

select *from stu_score
where no>=1 and no<=10
order by no;

select rownum,a.*
from lotte_product a
order by std_ym
;

select rownum,b.*
from (
select *from lotte_product order by std_ym
)b ;

select *from stu_score
order by no
;

-- kor 점수가 21등부터 30등 까지 출력하시오
select rnum,name,kor,eng,math,total,avg,rank,c_date
from (
select rownum rnum,b.*from
(select a.* from stu_score a
order by kor desc)b
)
where rnum>=21 and rnum<=30;
