-- 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.fullname, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
GROUP BY s.fullname, s.id
ORDER BY avg_grade DESC
LIMIT 5;

--1 студент із найвищим середнім балом з одного предмета.
SELECT d.name, s.fullname, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE d.id = 1
GROUP BY s.fullname, d.name
ORDER BY avg_grade DESC
LIMIT 1;

--Середній бал в групі по одному предмету.
SELECT d.name, gr.name, round(avg(g.grade), 2) AS avg_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3
GROUP BY gr.name, d.name
ORDER BY avg_grade DESC;

--Середній бал у потоці.
SELECT round(avg(g.grade), 2) AS avg_grade 
FROM grades g;

--Які курси читає викладач.
SELECT d.id, t.fullname, d.name 
FROM teachers t 
LEFT JOIN disciplines d ON t.id = d.teacher_id
WHERE t.id = 3;

--Список студентів у групі.
SELECT s.id, s.fullname, gr.name
FROM students s 
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE gr.id = 3;

--Оцінки студентів у групі з предмета.
SELECT s.id, d.name, gr.name, s.fullname, g.grade, g.date_of  
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3 AND gr.id = 3;

--Оцінки студентів у групі з предмета на останньому занятті.
SELECT g.date_of 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE g.discipline_id = 2 AND gr.id = 3
ORDER BY g.date_of DESC 
LIMIT 1;

SELECT s.id, d.name, gr.name, s.fullname, g.grade, g.date_of  
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN [groups] gr ON gr.id = s.group_id  
WHERE d.id = 3 AND gr.id = 3 AND g.date_of = (SELECT g.date_of 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN [groups] gr ON gr.id = s.group_id 
WHERE g.discipline_id = 3 AND gr.id = 3
ORDER BY g.date_of DESC 
LIMIT 1);

-- Список курсів, які відвідує студент
SELECT d.name, s.fullname 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
WHERE g.student_id = 1
GROUP BY d.name;

--Список курсів, які студенту читає викладач.
SELECT s.fullname, t.fullname, d.name 
FROM grades g  
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 1 AND g.student_id = 1
GROUP BY d.name;

--Середній бал, який викладач ставить студенту
SELECT DISTINCT s.fullname, t.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g  
LEFT JOIN students s ON s.id = g.student_id
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 1 AND s.id = 3
GROUP BY s.fullname;

--Середній бал, який ставить викладач
SELECT t.fullname, round(avg(g.grade), 2) AS avg_grade
FROM grades g  
LEFT JOIN disciplines d ON d.id = g.discipline_id
LEFT JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2
GROUP BY t.fullname;

SELECT *
FROM grades g  
JOIN disciplines d ON d.id = g.discipline_id
JOIN teachers t ON t.id = d.teacher_id;
