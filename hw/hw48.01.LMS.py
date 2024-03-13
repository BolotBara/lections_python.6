# Дана база данных произведений Шекспира, в которой содержатся следующие таблицы: character - герои произведений, work - произведения, chapter - главы произведений, paragraph - параграфы, wordform - слова, встречающиеся в произведениях
# Напишите следующие запросы:

# 1. Найдите 10 самых часто встречающихся слов.
# SELECT plaintext, occurences FROM wordform ORDER BY occurences DESC LIMIT 10

# 2. Найдите все слова, которые начинаются с буквы 'а', регистр не должен иметь значения.
# SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%' LIMIT 100

# 3. Найдите все произведения, которые относятся к жанру 'р'.
# SELECT * FROM work WHERE genretype ILIKE 'p%' LIMIT 100

# 4. Найдите среднее количество параграфов в произведения жанра t'.
# SELECT AVG(totalparagraphs) AS avg_paragraphs FROM work 
# WHERE genretype = 't' LIMIT 100

# 5. Выведите все произведения, в которых количество слов выше среднего.
# SELECT *FROM work
# WHERE totalwords > (SELECT AVG(totalwords) FROM work);

# 6. Выведите имя героя, количество его реплик, и произведение, в котором этот герой встречается.
# SELECT c.charname, c.speechcount, w.title
# FROM "character" c
# JOIN character_work cw ON c.charid = cw.charid
# JOIN work w ON cw.workid = w.workid;

# 7. Выведите среднее количество реплик героев в произведении 'Romeo and Juliet'.
# SELECT AVG(c.speechcount) AS avg_speechcount
# FROM "character" c
# JOIN character_work cw ON c.charid = cw.charid
# JOIN work w ON cw.workid = w.workid
# WHERE w.title = 'Romeo and Juliet';

# 8. Выведите общее количество слов в каждой из секций в таблице paragraph.
# SELECT section, SUM(wordcount) AS total_words
# FROM paragraph
# GROUP BY section;

# 9. Выведите всех героев, которые имеют от 15 до 30 реплик.
# SELECT *FROM "character"
# WHERE speechcount BETWEEN 15 AND 30;

# 10. Выведите все произведения, которые были написаны в 17 веке
# SELECT * FROM work
# WHERE year BETWEEN 1601 AND 1700;

# 11. Найдите все произведения, которые имею в полном названии слово 'the'
# SELECT *FROM work
# WHERE LOWER(longtitle) LIKE '%the%';

# 12. Выведите все уникальные секции в paragraph.
# select distinct section from paragraph

# 13. Для каждой главы введите: id, описание и название прозведения, к которой относится данная глава.
# SELECT ch.chapterid, ch.description, w.title
# FROM chapter ch
# JOIN work w ON ch.workid = w.workid;

# 14. Для каждого параграфа выведите: номер параграфа, имя героя, и количество реплик героя
# SELECT p.paragraphnum, c.charname, c.speechcount
# FROM paragraph p
# JOIN "character" c ON p.charid = c.charid;

# 15. Для каждого параграфа выведите: номер параграфа, название произведения и год выхода этого произведения.
# SELECT p.paragraphnum, w.title, w.year
# FROM paragraph p
# JOIN work w ON p.workid = w.workid;

