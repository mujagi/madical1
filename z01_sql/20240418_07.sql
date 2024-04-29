-- ���Ἲ ������� : �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- not null, unique, primary key, foreign key, check
-- ���̺� ����
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date DEFAULT sysdate
);

-- ������ �Է�, ���, ����, ���� �κ�
insert into member(memNo,id,pw,name,gender,mdate) values(
member_seq.nextval,'aaa','1111','ȫ�浿','����',sysdate
);

insert into member(memNo,id,pw,name,gender) values(
member_seq.nextval,'bbb','1111','������','����'
);

insert into member values(
member_seq.nextval,'ccc','1111','�̼���','����',sysdate
);

-- ���̺���� : �Խ��� ���̺���
create table board(
bno number(4) primary key,
id varchar2(30), -- �ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- �ܷ�Ű(foreign key)�� ��Ī : fk_id
references member(id) --member ���̺��� primary key id
);
-- primary key �� �����Ϸ��� freign key ��ϵǾ� �ִ� �����͸� �켱 ������ ����ؾ� ��.
-- primary key  �����Ǹ� ��� �����ϴ� ��� - on delete cascade, ��� �����ϴ� ��� - on update cascade

insert into board(bno,id,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values(
BOARD_SEQ.nextval,'aaa','�����Դϴ�.','�����Դϴ�.',sysdate,board_seq.currval,0,0,1,''
);

INSERT into board values(
BOARD_SEQ.nextval,'bbb','�����Դϴ�2.','�����Դϴ�2.',sysdate,board_seq.currval,0,0,1,''
);

insert into board(bno,id,btitle,bcontent,bgroup) values(
board_seq.nextval,'aaa','�����Դϴ�3.','�����Դϴ�3.',board_seq.currval
);

select *from board;

--����
delete board where bno = 3;

commit;

delete member where id = 'aaa';

-- decode ���ǹ�
select emp_name,department_id,
decode(department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40,'�λ��')
from employees
order by department_id asc;

select *from stu_score
order by avg desc;
-- 90��-a, 80��-b, 70��-c
select avg,
decode(avg,
90,'a',80,'b',70,'c')
from stu_score
order by avg desc;

--sh_clerk salary *15%,ad_asst *10% MK_rep *5%;
select job_id,salary,
decode(job_id,
'SH_CLERK',salary+(salary*0.15),
'PU_CLERK',salary+(salary*0.15),
'ST_CLERK',salary+(salary*0.15),
'SA_CLERK',salary+(salary*0.15),
'AD_ASST',salary+(salary*0.1),
'MK_REP',salary+(salary*0.05)
)as salary_up
from employees;

select department_id,department_name from departments;

-- job_id, clerk �� �� �ִ� job id�� �˻��Ͻÿ�
-- _ = �ڸ���
select job_id from employees
where job_id like '___CLERK'
;

select name,avg from stu_score;

select name,avg,
case 
when avg>=90 then 'A'
When avg>=80 then 'B'
when avg>=70 then 'C'
else 'F'
end as grade
from stu_score;

select department_id,department_name from departments;

select department_id,
case
when department_id = 10 then '�ѹ���ȹ��'
when department_id = 20 then '������'
when department_id = 30 then '����/�����'
when department_id = 40 then '�λ��'
when department_id = 50 then '��ۺ�'
when department_id = 60 then 'IT'
when department_id = 70 then 'ȫ����'
when department_id = 80 then '������'
when department_id = 90 then '��ȹ��'
when department_id = 100 then '�ڱݺ�'
when department_id = 110 then '�渮��'
when department_id = 120 then '�繫��'
when department_id = 130 then '������'
when department_id = 140 then '�ſ������'
when department_id = 150 then '�ֽİ�����'
when department_id = 160 then '���Ͱ�����'
when department_id = 170 then '������'
when department_id = 180 then '�Ǽ���'
when department_id = 190 then '�����'
when department_id = 200 then '���'
when department_id = 210 then 'IT ����'
when department_id = 220 then 'NOC'
when department_id = 230 then 'IT ��������ũ'
when department_id = 240 then '���� �ǸŻ����'
when department_id = 250 then 'IT �Ǹ���'
when department_id = 260 then 'ä����'
when department_id = 270 then '�޿���'
end as department_name
from employees
order by department_id asc;

select emp_name,department_id from employees;
select department_id,department_name from departments;

-- 2�� ���̺� ����
select emp_name,employees.department_id,department_name from employees,departments
where employees.department_id = departments.department_id
;

-- ������ ����Ͻÿ�
-- CLERK ���� : salary*15%, AD_ASST *10% , REP *5%,MAN*2%

select job_id,salary,
case
when job_id like '%CLERK%' then salary+(salary*0.15)
when job_id like '%AD_ASST%' then salary+(salary*0.10)
when job_id like '%REP%' then salary+(salary*0.05)
when job_id like '%MAN%' then salary+(salary*0.02)
end as F_salary
from employees
order by salary asc;

-- ���� ��� ���� 0.15 ����̻� 0.05 �λ��ؼ� ����Ͻÿ�
select job_id,salary,
case
when salary<=(select avg(salary) from employees) then salary+(salary*0.15)
when salary>=(select avg(salary) from employees) then salary+(salary*0.05)
end as f_salary
from employees;

-- case 2�� ���
select emp_name,salary,
case
when salary<=(select avg(salary) from employees) then 'up'
when salary>=(select avg(salary) from employees) then 'down'
end as salary_updown
,
case
when salary<=(select avg(salary) from employees) then salary+(salary*0.15)
when salary>=(select avg(salary) from employees) then salary+(salary*0.05)
end as salary_up
from employees
order by salary_up asc;


select *from stu_score;

select total,rank from stu_score
order by total desc;

-- rank() �Լ�
select total, rank, rank() over (order by total desc) as ranks from stu_score;
sekect no,rank() over (order by total desc) as ranks from stu_score;

select total,  rank from stu_score
order by total desc;

update stu_score set rank = 1
where total  = 291 
;

-- 1000�� ���� ���� �Է�
update stu_score a
set rank = (
select ranks from ( 
select no,rank() over (order by total desc) as ranks from stu_score
)b
where a.no = b.no
);

update stu_score 
set rank = ( 1

);

select no,rank from stu_score
order by no;

-- �׷��Լ� sum,avg,count,max,min     stddev ǥ������, variance �л�

-- ������ ����
select sum(salary) from employees;

select sum(kor) from stu_score;

select count(*) from employees;

select count(*) from employees
where department_id = 50;

-- Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�.
select count(*) from employees
where commission_pct is not null;

select *from employees emp;

-- ��ü �����
select count(*) from employees
where department_id = 50;

-- �μ����� �׷����� ����� ���
select department_id,count(department_id) from employees
group by department_id
order by department_id asc;

-- �÷��� grade
-- stu_score 90���̻� A 80�� �̻� B 70�� �̻� C, 60���̻� d, 60�� �̸� f
-- A���� ������� ���

select grade,count(grade) from 
(
select avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score
)
group by grade
order by grade asc
;


-- total ������ 91,92,93,94,.....99 - > 90 81,.....89->80
-- ����Ͻÿ�

select trunc(kor,-1),count(trunc(kor,-1)) from stu_score
where trunc(kor,-1) = 90
group by trunc(kor,-1)
order by trunc(kor,-1) asc;

select trunc(kor,-1),count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1);

select k_kor,count(k_kor) as k_count from
(select trunc(kor,-1) as k_kor from stu_score)
group by k_kor
;

select department_id,count(*) from employees
group by  department_id ;

select emp_name,count(emp_name) from employees;
group by emp_name ;

-- �μ��� ��� ������ ���Ͻÿ�.
select department_id,round(avg(salary),2) from employees
group by department_id
order by department_id;



select job_id,substr(job_id,4,length(job_id)-3) from employees;

select substr(job_id,4,length(job_id)-3),count(substr(job_id,4,length(job_id)-3)) as c_job_id from employees
group by substr(job_id,4,length(job_id)-3)
order by c_job_id;

-- �μ��� �ִ����, �ּҿ���, ��� ������ ����Ͻÿ�

select department_id,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees
group by department_id
order by department_id
;




select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

-- �μ��� �����, Ŀ�̼��� �޴� ��� �� ���
select *from employees;

select department_id,count(department_id), count(commission_pct) from employees
group by department_id
order by department_id
;

--having group by ������, where �Ϲ� �÷���������

select department_id,round(avg(salary),2) from employees
group by department_id
having avg(salary) >=6000
order by department_id;

-- emp_name �ι�° ���ڰ� a�� �����ϴ°��� ���� 
select department_id,round(avg(salary),2) from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= (select avg(salary) from employees)
order by department_id;

-- �μ��� �ִ������ 8000 �̻��ΰ͸� ���
select department_id,max(salary)from employees
group by department_id
having max(salary) >= 8000
order by department_id;

-- ����

select emp_name, department_id,salary from employees; 

select department_id, department_name from departments;

select count(*) from  employees ; 
select count(*) from departments;


-- ���̺� 2���� �����Ѱ� = ����
select *from employees,departments;

-- equi join
-- �� ���̺� ���� �÷��� ������ ���ؼ� �ش�Ǵ� �����͸� ���
-- equi join =107��  null 1�� �˻����� ����
select employee_id,emp_name,employees.department_id,department_name,salary 
from employees,departments
where employees.department_id = departments.department_id
;

select department_id,department_name from departments;

select id,name from member;
select id,btitle,bcontent from board;

update member set name = 'ȫ����'
where id = 'aaa';
select *from member;

--equi join
select bno,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile from board,member
where member.id = board.id
;
