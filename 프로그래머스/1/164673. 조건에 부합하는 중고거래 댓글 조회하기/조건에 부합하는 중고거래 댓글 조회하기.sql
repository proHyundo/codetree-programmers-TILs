-- 코드를 입력하세요
SELECT tb.TITLE, 
        tb.BOARD_ID, 
        tr.REPLY_ID, 
        tr.WRITER_ID, 
        tr.CONTENTS, 
        DATE_FORMAT(tr.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
FROM USED_GOODS_BOARD tb
    INNER JOIN USED_GOODS_REPLY tr 
        ON tb.BOARD_ID = tr.BOARD_ID
        AND DATE_FORMAT(tb.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY tr.CREATED_DATE ASC, tb.TITLE ASC;
