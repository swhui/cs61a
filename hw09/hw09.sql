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

-- copy your solution from prev hw!
-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes WHERE min < height AND height <= max;

-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT d.name
  FROM dogs AS d , parents AS p, dogs AS d1
  WHERE d.name = p.child AND p.parent = d1.name
  ORDER BY d1.height DESC;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT "REPLACE THIS LINE WITH YOUR SOLUTION";

  -- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT p1.child || ' and ' || p2.child || ' are ' || s2.size || ' siblings'
  FROM parents AS p1, parents AS p2, size_of_dogs AS s1, size_of_dogs AS s2
  WHERE p1.parent=p2.parent AND -- same parents
  s1.size = s2.size AND -- same size
  p1.child < p2.child AND --a then b
  p1.child = s1.name AND --match the names of first kid
  p2.child = s2.name; -- match names of second kid
