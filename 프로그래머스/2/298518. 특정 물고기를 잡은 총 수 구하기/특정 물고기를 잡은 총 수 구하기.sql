-- 코드를 작성해주세요

SELECT SUM(sub.cnt) as 'FISH_COUNT'
FROM (
    SELECT COUNT(ID) as cnt
    FROM FISH_INFO
    GROUP BY FISH_TYPE
    HAVING FISH_TYPE IN(
        SELECT FISH_TYPE
        FROM FISH_NAME_INFO
        WHERE FISH_NAME IN('BASS', 'SNAPPER')
    )
) as sub;
