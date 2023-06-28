.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = 'blue' and pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students group by smallest having count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color from students as a, students as b where a.pet = b.pet and a.song = b.song and a.time < b.time;


CREATE TABLE sevens AS
  SELECT students.seven from students, numbers where students.number = 7 and numbers.'7' = 'True' and students.time = numbers.time;


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price from products group by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) as low_price from inventory group by item;


CREATE TABLE shopping_list AS
  select item, store from lowest_prices where item in (SELECT name from products group by category having min(MSRP / rating));


CREATE TABLE total_bandwidth AS
  SELECT SUM(s.Mbs) AS Mb FROM stores s JOIN shopping_list sl ON s.store = sl.store;

