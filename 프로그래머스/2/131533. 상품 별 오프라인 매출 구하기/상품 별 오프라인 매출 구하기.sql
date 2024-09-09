-- 코드를 입력하세요
SELECT t_product.PRODUCT_CODE, SUM(t_product.PRICE * t_offline.SALES_AMOUNT) as SALES
FROM PRODUCT t_product
    JOIN OFFLINE_SALE t_offline ON t_product.PRODUCT_ID = t_offline.PRODUCT_ID
GROUP BY t_product.PRODUCT_CODE
ORDER BY SALES DESC, t_product.PRODUCT_CODE ASC;