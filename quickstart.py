from postbot import PostBot


def quickstart():
    """Quickstart script to start using PostBot in a jiffy"""

    post_bot = PostBot(
        geckodriver_path=r'/home/you/drivers/geckodriver',
        username='your_ig_account@email.com',
        password='your_ig_password',
        mysql_host='localhost',
        mysql_database='ig_posts_db',
        mysql_username='postman',
        mysql_password='ig_posts_db_passwd',
        mysql_posts_table='ig_posts',
        mysql_img_path_column='post_img_path',
        mysql_caption_txt_column='post_title'
    )

    # If you just want to post without the use of database, can instantiate PostBot without the MySQL data
    # post_bot = PostBot(geckodriver_path, 10)

    # Login to Instagram
    post_bot.login()

    # Make posts every 15 minutes using posts content stored in database
    post_bot.start_posting(15)

    # You can create one post at a time using create_post() function
    # post_bot.create_post("/your/img/path/post_image.jpg", "My first post here\n\n#programming #python #automation")

    post_bot.quit()


quickstart()
