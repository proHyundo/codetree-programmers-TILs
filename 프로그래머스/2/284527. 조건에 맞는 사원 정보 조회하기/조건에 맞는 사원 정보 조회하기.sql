-- 코드를 작성해주세요
 SELECT SUM(t_grade.SCORE) as 'SCORE', t_grade.EMP_NO as 'EMP_NO', t_emp.EMP_NAME as 'EMP_NAME', t_emp.POSITION as 'POSITION', t_emp.EMAIL as 'EMAIL'
 FROM HR_GRADE t_grade
     INNER JOIN HR_EMPLOYEES t_emp ON t_emp.EMP_NO = t_grade.EMP_NO
 WHERE t_grade.YEAR = '2022'
 GROUP BY t_grade.EMP_NO
ORDER BY SCORE DESC
 LIMIT 1;

