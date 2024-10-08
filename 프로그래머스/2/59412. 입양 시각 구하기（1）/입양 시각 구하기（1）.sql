-- 코드를 입력하세요
# SELECT DATE_FORMAT(DATETIME, '%H')
# FROM ANIMAL_OUTS

SELECT DATE_FORMAT(DATETIME, '%H') as HOUR, COUNT(ANIMAL_ID)
FROM ANIMAL_OUTS
GROUP BY DATE_FORMAT(DATETIME, '%H')
HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR