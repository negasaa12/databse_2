### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?


 PostgreSQL is often referred to simply as Postgres and is a powerful tool for managing and organizing large volumes of data. 

- What is the difference between SQL and PostgreSQL?

 SQL is a language used to interact with databases, while PostgreSQL is a specific database management system that supports the SQL language and provides additional features and functionality


- In `psql`, how do you connect to a database?

you use psql name_of_database

- What is the difference between `HAVING` and `WHERE`?

 WHERE filters individual rows, while HAVING filters groups formed by the GROUP BY clause. WHERE is used before the grouping operation, while HAVING is used after the grouping operation.

- What is the difference between an `INNER` and `OUTER` join?


inner join only returns the matching rows, while outer join returns all the rows from one table and the matching rows from the other table, including any non-matching rows. 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?

 the main difference between a LEFT OUTER join and a RIGHT OUTER join is the direction in which the tables are joined.

- What is an ORM? What do they do?


An ORM tool provides an abstraction layer between the application code and the database, which allows developers to work with database objects in a more object-oriented way


- What are some differences between making HTTP requests using AJAX

Overall, AJAX can provide a more responsive and efficient user experience, while traditional page loads may be simpler to implement but can result in slower load times and a less optimal user experience.


  and from the server side using a library like `requests`?

- What is CSRF? What is the purpose of the CSRF token?

CSRF is a web vulnerability where an attacker trick a user  into unknowingly performing an action on a website that the user authenticated to. CSRF token matches the expected value, which ensures that the request was sent from the same client that received the token. 

- What is the purpose of `form.hidden_tag()`?

In Flask, form.hidden_tag() is a function that generates a hidden input field containing a token that is used to protect against CSRF attacks.
