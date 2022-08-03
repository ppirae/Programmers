SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE (NAME like "Lucy" OR
       NAME like "Ella" OR
       NAME like "Pickle" OR
       NAME like "Sabrina" OR
       NAME like "Mitty")