--trunc ���� round  �ݿø�
select sysdate,hire_date,round(sysdate-hire_date,3) from employees;

--���� sysdate -1 ���� sysdate+1
select sysdate-1 ����, sysdate ����, sysdate+1 ����,sysdate+100 from dual;

--���� m_no ��������ȣ, m_yesterday,m_today,m_tomorrow,m_year ��¥ �÷��� ���� ���̺� m_date
-- ����, ����, ����, 1�� �� ��¥�� �����Ͻÿ�

create sequence seq_m_no
increment by 1
start with 1
minvalue 1
maxvalue 9999
nocycle
nocache;

create table m_date(
m_no number(4),
m_yesterday date,
m_today date,
m_tomorrow date,
m_year date
);

insert into m_date values(
seq_m_no.nextval,sysdate-1,sysdate,sysdate+1,sysdate+365
);

select *from m_date;

-- abs ���밪, ceil,round,floor round,trunc - �ڸ���
select abs(hire_date-sysdate) from employees;

-- ��¥�� ���� �������� �ݿø�
select hire_date,round(hire_date,'month') from employees;

-- ��¥�� ���� �������� ����
select hire_date,trunc(hire_date,'month') from employees;

select trunc(hire_date,'month') ������ ,hire_date from employees
order by hire_date;

select *from channels;

drop table stu_score;

select period,count(period) from kor_loan_status
group by period
order by period;

select period from kor_loan_status
where period = '201111';

select *from students;

select trunc(kor,-1) t_kor, count(trunc(kor,-1)) count from students
group by trunc(kor,-1)
order by t_kor;

select *from stu_score
order by no;

update stu_score set name = '������'
where no=10;

-- 2���� ��¥  �� ������ Ȯ��
select hire_date,floor(months_between(sysdate,hire_date)),trunc(sysdate-hire_date,2) from employees;

-- ���� �߰�
select hire_date, add_months(hire_date,6) from employees;

-- last day
select hire_date,last_day(hire_date),round(hire_date,'d') from employees;

select sysdate, trunc(sysdate,'d') from employees;

-- ������, ó����, ��������
select sysdate ������,trunc(sysdate,'month') ó����,last_day(sysdate) �������� from dual;

-- Ư�� ������ ��¥�� Ȯ��
select sysdate, next_day(sysdate,'�����') from dual;

-- ������ ó�� ���� ��¥
select sysdate, trunc(sysdate,'d'),next_day(sysdate,'�����') from dual;


drop table board;

-- board ���̺� default�� �Է� ���� �� ������ ������ �ڵ� �Էµ�
create table board(
bno number(4) primary key, -- �ߺ��� �ȵ�, null���� ������� ����, �⺻Ű�� ����
bname varchar2(30),
btitle varchar2(1000),
bcontent clob, --varchar2(3000)�� �Ѱ� clob - ������, varchar2�� Ÿ��
bdate date default sysdate,
bhit number default 0,
bgroup number,
bstep number default 0,
bindent number default 0,
bfile varchar2(100)
);

insert into board values(
board_seq.nextval,'aaa','�����Դϴ�.','�����Դϴ�.',sysdate,0,board_seq.currval,0,0,'1.jpg'
);

insert into board(bno,bname,btitle,bcontent,bgroup,bfile) values(
board_seq.nextval,'bbb','�̺�Ʈ ��û','�̺�Ʈ�� ��û�մϴ�.',board_seq.currval,'2.jpg'
);

select *from board;

--����ȯ - number,character,date

select sysdate from dual;
select sysdate, to_char(sysdate,'yyyy-mm-dd hh:mi:ss') from dual;
select to_char(sysdate,'yy/mm/dd') from dual;
select to_char(sysdate,'yyyy') from dual;

--���ڿ� +�� �ȵ� ko+2024+0001
select 'ko'||to_char(sysdate,'yyyy')||trim(to_char(seq_mno.nextval,'0000')) from dual;

select to_char(sysdate,'dy'),to_char(sysdate,'day') from dual;

select to_char(sysdate,'yyyy-mm-dd hh:mi:ss mon day') from dual;

--hire_date, ����� ��¥ ���� �ؼ� ���
select to_char(hire_date,'yyyy-mm-dd mon day') from employees;

-- am,pm ���� ���� hh24 = 24�ð����� ǥ��
select to_char(sysdate,'pm hh24:mi:ss') from dual;


select *from stu_score;

select to_char(c_date,'yyyy-mm-dd hh:mi:ss day') from stu_score
order by c_date;

-- ��¥���� ��� �����Ͱ� �� �ִ��� ����Ͻÿ�.
select c_date,count(c_date) from stu_score 
group by c_date
order by c_date;

-- ������(to_char) ��Ģ����(+,-,*,/) �ȵ�. �ڸ��� ǥ��, ��ǥ ǥ��, ��¥���� ǥ��
-- ������(to_nuber) ��Ģ���� ���� �÷��� ��Ģ���� ���� �ڸ��� ǥ��(0001), ��ǥ ǥ�� �ȵ�
-- ��¥��(to_date) +,- ���갡��, months_between 2�� ��¥ �� ��� ����, ��¥������ �����ؼ� ����� �ȵ�


-- �������̶� �ȿ� �ִ� �����Ͱ� �����̸� �ڵ����� ����ȯ�ؼ� �������.
-- ������ �ȿ� ���ڰ� ������ �Ұ���
select 10 a,100 b,(10+100) ab,to_char(100),10+to_char(300) from dual; --����
select 10 a,100 b,(10+100) ab,to_char(100),10+'300��' from dual; --�Ұ���

-- '0000' ���ڸ��� 0���� ä��, '9999' ���ڸ��� ���ڸ� ��
select 12340000,to_char(12340000),length(to_char(12340000,'999,999,999')) from dual;
select length(12340000),to_char(12340000),length(to_char(12340000,'000,999,999')) from dual;

--l�� ��ȭ ǥ�� (�������� �ٸ�)
select 12340000,to_char(12340000,'L999,999,999') from dual;
--$�� $ ǥ��
select 12340000,to_char(12340000,'$999,999,999') from dual;
-- �Ҽ��� �ڸ� ǥ��
select 1234.1234,to_char(1234.1234,'000,999.99') from dual;
-- 10�� �ڸ��� ǥ��
-- ���������ؼ� �ڸ��� Ȯ�� trim
select length(trim(to_char(12345,'0000000000'))),length(trim(to_char(12345,'999,999'))) from dual;

--����
--123,456,789 + 100,000 = ���� ���, õ���� ǥ���Ұ�

select 123456789 num1, 100000 num2,to_char(123456789+10000,'l999,999,999')�� from dual;
select to_char(to_number(replace('123,456,789',',',''))+to_number(replace('100,000',',','')), 'L999,999,999'  )
from dual;

select to_number('0000123') from dual;

-- ��¥��
-- �������� ��Ģ���� x
select '2024-04-24'-'2024-04-23' from dual; -- �ȵ�
select to_date('2024-04-24')-to_date('2024-04-23') from dual; -- to_date�� ��ȯ �� ����
select to_date('2024/04/24')-to_date('2024/04/23') from dual;
-- 24/04/01 �� �ڵ� ��ȯ
select to_date('20240401') from dual;

-- ����
--2024-04-01 Ÿ������ ��ȯ�ؼ� ����Ͻÿ�
select to_date('20240401') from dual;
select to_char(to_date('20240401'),'yyyy-mm-dd') from dual;


-- �������� ���� �Լ�
select length('�ȳ��ϼ���') from dual;
select length(1234000) from dual;

select hire_date from employees
where hire_date >= '20080101'
;

select *from stu_score;

select c_date from stu_score
where c_date = '2024/04/11'
;

select sysdate-hire_date from employees;
select sysdate-to_date('2024/04/01') from dual;

--����
--20,000 - 10,000 ������ 10,000 ���

select to_char(to_number('20,000','99,999')-to_number('10,000','99,999'),'99,999') from dual;

--����
select commission_pct from employees;

--���� ���� = ���� + (����*Ŀ�̼�) ���������ؼ� ����Ͻÿ�
--nvl(������,0)
select salary+(salary*nvl(commission_pct,0)) from employees;

-- coommission_pct null ���� ����Ͻÿ�
select emp_name,commission_pct from employees
where commission_pct is null;

select manager_id from employees
order by manager_id desc;

-- ����
--manager_id null �̸� 0
select nvl(manager_id,0) from employees
order by manager_id desc;

-- ���� manager_id null �̸� ceo�� �Է��Ͻÿ�
select nvl(to_char(manager_id),'ceo') from employees
order by manager_id desc;
