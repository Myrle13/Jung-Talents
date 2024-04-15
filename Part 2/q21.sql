SELECT * FROM ORDERS;
SELECT * FROM PRODUCT;

SELECT CATEGORY, SUM(SALES) as SALE,
round(sum(sales) * 100 / sum(sum(sales)) over (),2) as '%'
FROM PRODUCT, ORDERS
WHERE PRODUCT.ID = ORDERS.PRODUCT_ID
GROUP BY product.category
order by SALE desc;

SELECT CATEGORY,
CONCAT(round(sum(sales) * 100 / sum(sum(sales)) over (),2), '%') AS '%',
round(round(sum(sales) * 100 / sum(sum(sales)) over (),2)* 2000 /100) as Spread
FROM PRODUCT, ORDERS
WHERE PRODUCT.ID = ORDERS.PRODUCT_ID
GROUP BY category 
order by sum(sales) desc;

SELECT CATEGORY ,
CONCAT(round(sum(sales) * 100 / sum(sum(sales)) over (),2), '%') AS '%',
round(round(sum(sales) * 100 / sum(sum(sales)) over (),2)* 2000 /100)  as Spread
FROM PRODUCT, ORDERS
WHERE PRODUCT.ID = ORDERS.PRODUCT_ID
GROUP BY CATEGORY 
order by sum(sales) desc;

WITH Temp AS(
              SELECT CATEGORY ,
          CONCAT(round(sum(sales) * 100 / sum(sum(sales)) over (),2), '%') AS Per,
          round(round(sum(sales) * 100 / sum(sum(sales)) over (),2)* 2000 /100) as Spread
          FROM PRODUCT, ORDERS
		  WHERE PRODUCT.ID = ORDERS.PRODUCT_ID
          GROUP BY CATEGORY 
		  order by sum(sales) desc
)
SELECT  Category, Per  , Spread  FROM Temp
UNION ALL
SELECT 'Grand Total', Sum(per), SUM(Spread)  FROM Temp;


select O1.PRODUCT_ID, O2.PRODUCT_ID, count(distinct O1.ORDER_ID) as COUNT
from ORDERS O1 join
     ORDERS O2
     on O1.ORDER_ID = O2.ORDER_ID and
        O1.PRODUCT_ID < O2.PRODUCT_ID
group by O1.PRODUCT_ID, O2.PRODUCT_ID
having count(distinct O1.ORDER_ID) >=2
order by COUNT desc;
