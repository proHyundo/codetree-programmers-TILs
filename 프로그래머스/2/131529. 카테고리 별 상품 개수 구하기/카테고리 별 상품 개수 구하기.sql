-- 코드를 입력하세요

SELECT SUBSTRING(PRODUCT_CODE, 1, 2) as 'CATEGORY', COUNT(*) as 'PRODUCTS'
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;

# HELP SUBSTRING;

# mysql> SELECT SUBSTRING('Quadratically',5); -> 'ratically' 
# mysql> SELECT SUBSTRING('foobarbar' FROM 4); -> 'barbar' 
# mysql> SELECT SUBSTRING('Quadratically',5,6); -> 'ratica' 
# mysql> SELECT SUBSTRING('Sakila', -3); -> 'ila' 
# mysql> SELECT SUBSTRING('Sakila', -5, 3); -> 'aki' 
# mysql> SELECT SUBSTRING('Sakila' FROM -4 FOR 2); -> 'ki'