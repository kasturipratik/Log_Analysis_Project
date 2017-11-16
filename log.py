import psycopg2

DBNAME = "news"


# Method to sort out the most viewed articles
def get_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
            SELECT articles.title, count(log.status) as count
            FROM articles, log
            WHERE log.status = '200 OK'
              and log.path like '%' || articles.slug || '%'
            GROUP BY articles.title
            ORDER BY count desc
            limit 3;
        """)
    posts = c.fetchall()
    db.close()
    print("\n List of articles as per their views: \n")
    for post in posts:
        print("  %s     : %s views" % (str(post[0]), str(post[1])))


# Method to sort out the most popular author
def get_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
            SELECT authors.name, count(log.status) as count
            FROM articles, log, authors
            WHERE log.status = '200 OK'
              and log.path like '%' || articles.slug || '%'
              and authors.id = articles.author
            GROUP BY authors.name
            ORDER BY count desc;
        """)
    posts = c.fetchall()
    print(" \n List of authors with the most popular "
          "article authors of all time: \n")
    db.close()
    for post in posts:
        print("  %s : %s views" % (str(post[0]), str(post[1])))


# Method to sort out the error that happened more tha 1% of the time in a day
def get_error():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()

    c.execute("""
            SELECT total.date,
            ((100.0*error.count)/total.day_views) as count
            from total,error
            where total.date = error.date and
            ((100.0*error.count)/total.day_views) > 1
            order by count desc;
        """)
    posts = c.fetchall()
    db.close()
    print("\n On which days did more than 1% of requests lead to errors \n")
    for post in posts:
        print("  %s : %s \n " % (post[0], round(post[1], 2)))


get_articles()
get_authors()
get_error()
