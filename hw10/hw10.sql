CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  select parents.child from parents, dogs where dogs.name = parents.parent order by dogs.height desc;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT dogs.name as name, sizes.size as size from sizes, dogs where dogs.height > sizes.min and dogs.height <= sizes.max order by dogs.name asc;


CREATE TABLE siblings AS
  SELECT a.child as a, b.child as b from parents b, (select * from parents group by parent) a where a.parent = b.parent and a.child != b.child;

CREATE TABLE sentences AS
  SELECT "The two siblings, " || s.a || " plus " || s.b || " have the same size: " || d.size from siblings s, size_of_dogs d, size_of_dogs e where s.a = d.name and s.b = e.name and d.size = e.size;