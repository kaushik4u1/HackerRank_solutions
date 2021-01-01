/*
Enter your query here.
*/

SELECT concat(NAME, CASE WHEN occupation = "Doctor" THEN "(D)" WHEN occupation = "Professor" THEN "(P)" WHEN occupation = "Singer" THEN "(S)" WHEN occupation = "Actor" THEN "(A)" END )
FROM OCCUPATIONS 
ORDER BY NAME;

select concat('There are a total of',concat(' ',concat(count(occupation),concat(' ',concat(lower(occupation),'s.'))))) as total 
from occupations
group by occupation 
order by total;
