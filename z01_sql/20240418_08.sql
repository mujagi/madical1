select *from stu_score
where name like '_a%'
order by no asc;

select board.id,member.name from board,member

where board.id = member.id ;

select bno, a.id, name, btitle, bcontent,bdate,bgroup,bstep,bindent,bhit,bfile
from board a,member b;

select no,name,total,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'c'
when avg >= 60 then 'd'
else 'f'
end as grade
from stu_score ;

select *from stu_score;

select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)),to_char((salary+(salary*nvl(commission_pct,0)))*1410,'999,999,999l') from employees ;
select *from departments;

select department_id,avg(salary),max(salary),min(salary) from employees
where department_id is not null
group by department_id
order by department_id
;

select *from stu_score
where name like '%ȫ%';

-- ȫ�̶�� �˻��ϸ� ȫ�� ���õ� �л��� ��� ��µǵ��� �Ͻÿ�.

select *from stu_score
where avg>=60
;

-- �����ȣ, �����, �μ���ȣ, �μ����� ����Ͻÿ�.
select employee_id,emp_name,employees.department_id,department_name
from employees,departments
where employees.department_id = departments.department_id and emp_name like '_a%'
and salary>=(select avg(salary) from employees)
;

-- �׸���, �ι�° �ڸ��� a�� ���� ����� �˻��Ͻÿ�.
select emp_name from employees
where emp_name like '_a%'
;

-- ������ ��� �̻��� ����� �˻��Ͻÿ�
select salary from employees
where salary>=(select avg(salary) from employees)
;

select *from employees;
select *from departments;
select *from jobs;

-- �����ȣ e, ����� e, �μ���ȣ e, �μ��� d, ���޹�ȣ e, ���޸� jobs ����Ͻÿ�.

select employee_id,emp_name,e.department_id,department_name,e.job_id,job_title from employees e,departments d,jobs j
where e.department_id = d.department_id 
and e.job_id = j.job_id
order by department_id
;