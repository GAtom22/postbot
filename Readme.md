# PostBot
*A simple tool to make posts on Instagram programmatically*

---

### Installation

>`pip install postbot` or `pip3 install postbot`

### Description

This tool provides capabilities to make posts on instagram according to content stored in a database 
and a defined time interval.

For example, let's suppose that you already have many images which you 
want to post and its corresponding caption text and tags. And you are planning
to post them on Instagram one each day. So you can store this information in a database
and **PostBot** automates this task in a few lines of code:

<pre><code>
from postbot import PostBot
<br>
<br>def quickstart():

    <br># 1 - Create an instance of PostBot
    <br>    post_bot = PostBot(
    <br>    geckodriver_path=r'/home/you/drivers/geckodriver',
    <br>    username='my_ig_account@mail.com',
    <br>    password='my_password',
    <br>    mysql_host='localhost',
    <br>    mysql_database='posts_db',
    <br>    mysql_username='postman',
    <br>    mysql_password='post_db_pass',
    <br>    mysql_posts_table='posts_table',
    <br>    mysql_img_path_column='post_img_path',
    <br>    mysql_caption_txt_column='post_txt'
    <br>    )
    
    <br># 2 - Login to Instagram
    <br>post_bot.login()

    <br># 3 - Start posting
    <br># This function makes a post every amount of minutes specified (1 day = 1440 minutes)
    <br>minutes_in_a_day = 1440
    <br>post_bot.start_posting(minutes_in_a_day)

    <br>post_bot.quit()
    <br>
</code></pre>

That's it! The bot will run till all posts have been posted.

Take into consideration that the database table that has the posts needs a **'posted'** column
of type boolean with default value of *false*. This is used by the **PostBot** to keep track of the posted posts
and the pending ones.

---

>**Disclaimer**: Please note that this is a research project. The owner and contributor/s of this project are by
> no means neither responsible for any usage of this tool nor responsible if your account gets banned due to the extensive
> use of this tool. Use it at your own risk.


