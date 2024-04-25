-- ����, ����, ����
select sysdate-1,sysdate,sysdate+1 from dual;
-- ����, �̴��� ù��, �̴��� ��������
select sysdate,trunc(sysdate,'month'),last_day(sysdate) from dual;
-- �� ��¥�� �ϼ�, �� ��¥�� �� ��
select round(sysdate-hire_date,3), trunc(months_between(sysdate,hire_date),2) from employees;
-- trunc �ϴ��� ����
select trunc(kor,-1) kor, count(trunc(kor,-1)) from stu_score
group by trunc(kor,-1)
order by kor;
-- ���� hire_date ��¥���� ���� ����Ͻÿ�.
select to_char(hire_date,'yyyy-mm-dd') from employees;
select to_char(hire_date,'mm') hire_date, count(to_char(hire_date,'mm'))from employees
group by to_char(hire_date,'mm')
order by hire_date;
-- ���� hire_date yyyy �⵵, �⵵�� �ο� ���� ����Ͻÿ�.
select to_char(hire_date,'yyyy') hire_date, count(to_char(hire_date,'yyyy')) from employees
group by to_char(hire_date,'yyyy')
order by hire_date;
-- ����ȯ - number, charactermdate
-- number ��Ģ���갡��, ��ǥǥ�þȵ�, ��ȭǥ�þȵ�.
-- char ��Ģ����(+,-) �ȵ�, ��ǥǥ�ð���, ��ȭǥ�ð���
-- date +,- ���� / ���� ������´� ����Ұ�
-- ������ ���·� �й��� �ο��Ͻÿ�.
-- stu_seq �������� ������ 5���� �й��� ����غ�����
-- ko+2024+0001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(stu_seq.nextval,'0000')) from dual;
-- (123,456,789)+(156,778) = ? ����Ͻÿ�.
-- (123,456,789)+(100,000) = 123556789 ����Ͻÿ�.
select to_number(replace('123,456,789',',',''))+to_number(replace('156,778',',','')) from dual;
select to_char(to_number('123,456,789','999,999,999')+to_number('100,000','999,999'),'999,999,999') from dual;
select to_char(salary,'$999,999') salary from employees;

--����Ÿ���� ��¥Ÿ������ ����
select 20240425+3 from dual; -- ����Ÿ��
select to_char(20240425+3) from dual; --����Ÿ��
select to_date(20240425+3) from dual; --��¥Ÿ��

-- ����Ÿ���� ��¥Ÿ������ ����
select emp_name,hire_date from employees
where hire_date >to_date(20070101)
order by hire_date;

--���� 01,02,08�� �Ի������鼭 �̸� 2��°�� a�� ���ִ� ������
select emp_name,hire_date from employees
where to_char(hire_date,'mm') in ('01','05','08') and emp_name like '_a%';

--����, 20070101 ���� �Ի��� ����̸� a�� ���ִ� ����� ����Ͻÿ�.
select emp_name,hire_date from employees
where hire_date>to_date(20070101) and emp_name like '%a%'
order by hire_date;

--����Ÿ���� ��¥Ÿ������ ����
select sysdate - to_char('20240401') from dual;

select sysdate,'2024-04-01', sysdate-to_date('2024-04-01') from dual;

select *from m_date;



create table eventDate(
eno number,
e_today date,
e_choice_day date,
e_period number
);

--�Է½� ��¥ Ÿ�Կ� ����(���� = ��¥����)�� �Է��ص�����
-- ��¥�� ���ڸ� ����� �Ұ���, �׷��� ���ڸ� ��¥Ÿ������ �����ؾ� ��.
insert into eventDate values(
seq_mno.nextval,'2024-04-01',sysdate,sysdate-to_date('2024-04-01')
);

select *from eventDate;

--����Ÿ���� ����Ÿ������ ����
select to_number('20,000','99,999')-to_number('10,000','99,999') from dual;

--null�� 0���� ġȯ nvl()
select salary,commission_pct,salary+(salary*nvl(commission_pct,0)) from employees;

--manager_id null ceo
select manager_id from employees
order by manager_id desc;

--����Ÿ���� ����Ÿ������ ����
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;

--�׷��Լ� : count,sum,avg,min,max


-- �׷��Լ� count(���) = �Ѱ���
select count(emp_name) from employees;
select count(*) from employees; -- count(*) null�� ���� ���
select count(manager_id) from employees; --107���� ���������� null ���� ������ �ȵǼ� 106���� ���
select emp_name,manager_id from employees;

-- sum : ����
select sum(salary) from employees;
select to_char(sum(salary),'999,999') from  employees;

-- avg : ���
select avg(salary) avg_sal from employees;

-- min : �ּҰ�, max : �ִ밪
select min(salary), max(salary) from employees;

--����
--6461 �޷����ٳ��� ����� ����Ͻÿ�
select emp_name,salary from employees
where salary> (select avg(salary) avg_sal from employees) 
order by salary;

-- ���� �Լ�, �׷��Լ��� ���� ����� �ȵ�
select emp_name,min(salary) from employees;

--�����ּҿ����� �޴� ����� �̸��� ����Ͻÿ�
select employee_id,emp_name,salary from employees
where salary = (select min(salary) from employees);

- ���� �ִ���� �޴� ����� ���, �̸� ���
select employee_id,emp_name,salary from employees
where salary = (select max(salary) from  employees);

-- �μ���ȣ�� 50���� ����� ��ü �հ�
select department_id,salary from employees;

select sum(salary) from employees
where department_id = 50;

select count(*) from stu_score;

-- ���� kor������ 80�� �̻��� �л��� ����Ͻÿ�
select name,kor from stu_score
where kor>=80 
order by kor;
-- ����, ������������ �������� ����̻�, �������� ����̻��� �л��� ����Ͻÿ�
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

-- ���� ���� �ִ�, �ּ� ���, ����� ��� ���

select emp_name,salary from employees
where salary = (select max(salary) from employees) or 
salary = (select min(salary) from employees) or
salary = (select max(salary) from ( 
select emp_name,salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc));




--��պ��� ���� �� �� ���� ���� ��ã��
select max(salary) from ( 
select emp_name,salary from employees
where salary <= (select avg(salary) from employees)
order by salary desc);

-- �����Լ�
-- lpad
select emp_name,lpad(emp_name,15,'#') from employees; -- lpad: ���ʿ� �����ڸ��� ��ŭ '#' ä��
select emp_name,rpad(emp_name,20,'@') from employees; -- rpad: �������� �����ڸ��� ��ŭ '@' ä��

select emp_name,ltrim(emp_name,'Do')from employees; -- ltrim: emp_name �� ������ 'Do' �� �߶���

select 'ko20240001',ltrim('ko20240001','ko2024') from dual;

select emp_name, substr(emp_name,3,4) from employees; -- substr : (���,����,�߶�� ����) �������� �����ؼ� �߶�� ������ �߶�´�

select job_id from employees;
select *from employees;
--���� job_id sh�� �����ȣ�� �����ؼ� ����Ͻÿ�
select substr(job_id,1,2)||employee_id from employees; 

--length : ���ڿ��� ����
select emp_name, length(emp_name) from employees
where length(emp_name)>15;

--��¥ �Լ�
-- ��¥������ +,- ���� =����
select sysdate+1 from dual;
-- ��¥������ - ��¥������ = ����
select sysdate-hire_date from employees;
-- ��¥������ + ��¥������ = �Ұ���
select sysdate+hire_date from employees;

select sysdate,trunc(sysdate,'month'),round(sysdate,'month') from dual;

select round(sysdate,'year') from dual;

-- ������ �߰�,���
select sysdate,add_months(sysdate,3) from dual;
select sysdate,add_months(sysdate,-2) from dual;

-- ceil : �ø�, floor : ����, mod : ������, power : ����
select ceil(-4.2),floor(-4.2),mod(8,3),power(2,10) from dual;

--����  ���̺��� ����̸� �Ի��� 
select *from employees;
select emp_name,hire_date from employees;

select emp_name,hire_date,emp_name||to_char(hire_date,' YYYY"��"MM"��"DD"��"') from employees;

-- ����, �����,�ڸ��� 9�ڸ�,����� 0���� ǥ��,����*1400 �տ� ����ǥ�ÿ� ��ǥ�� �־� ����Ͻÿ�.
select emp_name,salary,to_char(salary*1400, 'L000,000,000') from employees;

-- �ڽ��� ���ϰ� �ڽ��� ������ ���� ���� ������ ��¥
select trunc(to_date('2010-10-10'),'month'),'2010-10-10',last_day('2010-10-10') from dual;

select *from member;

desc member;

--colum �߰�, ����, ����
--commit,rollback�� �ȵ� �ٷ� �����
alter table member add gender varchar2(6) default 'female' not null;

-- �÷����� commit, rollback �� ����.
alter table member drop column phone;

-- �÷����� : �÷��̸�, Ÿ�Ժ���
alter table member rename column name to stu_name; -- �̸�����
alter table member modify(stu_name varchar2(50));  -- Ÿ�Ժ���
alter table member modify(stu_name varchar2(3)); --������ ���ڿ��� �����Ϸ��� ũ�⸦ �ѱ� ������ ���� �Ұ���, �������� ����
alter table member modify(stu_name number(100)); -- �ٸ� Ÿ������ �����Ϸ��� ��� �����͸� ����� �Ǵ� null �� ���� �� Ÿ�Ժ����ؾ� ����

update member set gender = 'male' ;

commit;
