-- 코드를 입력하세요
SELECT s.sit as INGREDIENT_TYPE, SUM(s.sto) as TOTAL_ORDER
FROM (
SELECT t_info.INGREDIENT_TYPE as sit, SUM(t_half.TOTAL_ORDER) as sto
FROM FIRST_HALF t_half INNER JOIN ICECREAM_INFO t_info ON t_half.FLAVOR = t_info.FLAVOR
GROUP BY t_half.FLAVOR
    ) as s
    GROUP BY s.sit