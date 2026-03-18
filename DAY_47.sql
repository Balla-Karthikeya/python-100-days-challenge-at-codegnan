create database student_instagramDB;

use student_instagramDB;
-- USERS TABLE
CREATE TABLE USERS(USERID INT PRIMARY KEY AUTO_INCREMENT,
					USERNAME VARCHAR(50) UNIQUE NOT NULL, 
                    EMAIL VARCHAR(100) UNIQUE NOT NULL, 
                    PASSWORD VARCHAR(20) NOT NULL, 
                    BIO TEXT, 
                    CREATESAT DATETIME DEFAULT current_timestamp);
-- POSTS TABLE
CREATE TABLE POSTS(POSTID BIGINT PRIMARY KEY AUTO_INCREMENT,
					USERID INT,
                    CAPTION TEXT,
                    LIKES_COUNT INT DEFAULT 0,
                    CREATEDAT TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    foreign key(USERID) REFERENCES USERS(USERID)
                    );
-- COMMENTS TABLE
CREATE TABLE COMMENTS(COMMENTID INT PRIMARY KEY AUTO_INCREMENT,
						POSTID BIGINT,
                        USERID INT,
                        COMMENTTEXT VARCHAR(255) NOT NULL,
                        CREATEDAT DATETIME DEFAULT CURRENT_TIMESTAMP,
                        foreign key(POSTID) REFERENCES POSTS(POSTID),
                        foreign key(USERID) REFERENCES USERS(USERID)
                        );
					
INSERT INTO USERS (USERNAME, EMAIL, PASSWORD, BIO) VALUES
('karthik', 'karthik@gmail.com', 'pass123', 'AI student and coder'),
('rahul', 'rahul@gmail.com', 'rahul123', 'Love travelling'),
('ananya', 'ananya@gmail.com', 'ana123', 'Photographer'),
('sneha', 'sneha@gmail.com', 'sneha123', 'Food blogger'),
('arjun', 'arjun@gmail.com', 'arjun123', 'Fitness enthusiast'),
('meera', 'meera@gmail.com', 'meera123', 'Artist'),
('vikram', 'vikram@gmail.com', 'vikram123', 'Tech geek'),
('pooja', 'pooja@gmail.com', 'pooja123', 'Fashion lover'),
('rohit', 'rohit@gmail.com', 'rohit123', 'Cricket fan'),
('isha', 'isha@gmail.com', 'isha123', 'Nature lover');

INSERT INTO POSTS (USERID, CAPTION, LIKES_COUNT) VALUES
(1, 'Learning SQL databases today!', 25),
(2, 'Beautiful sunset view 🌅', 40),
(3, 'My latest photography shot', 35),
(4, 'Trying a new recipe today', 28),
(5, 'Morning workout done 💪', 50),
(6, 'Finished a new painting', 32),
(7, 'Exploring new AI tools', 45),
(8, 'New fashion outfit', 38),
(9, 'Watching cricket match', 30),
(10, 'Nature walk today 🌿', 27);

INSERT INTO COMMENTS (POSTID, USERID, COMMENTTEXT) VALUES
(1, 2, 'Nice post!'),
(2, 3, 'Amazing view'),
(3, 4, 'Great photography'),
(4, 5, 'Looks tasty!'),
(5, 6, 'Keep going!'),
(6, 7, 'Beautiful artwork'),
(7, 8, 'Very informative'),
(8, 9, 'Nice outfit'),
(9, 10, 'Enjoy the match'),
(10, 1, 'Nature is peaceful');


select *from users;  
select *from posts;


-- maximum likes post 
-- 1.total number of users
SELECT COUNT(*) AS total_users FROM USERS;

-- 2.total numbers of posts
select count(*) as total_posts from posts;

-- 3. average likes per posts
select round(avg(likes_count),2) as average_likes from posts;

-- 4. maximum followers count
select *from posts 
where likes_count = (select max(likes_count) from posts);

select *from posts 
where likes_count = (select likes_count from posts 
					order by likes_count desc limit 1 offset 1);

-- 5. minimum post count by a user 

SELECT userid, COUNT(*) AS post_count FROM posts
GROUP BY userid ORDER BY post_count
LIMIT 20;


SELECT u.userid, u.username, COUNT(*) AS post_count
FROM posts p
INNER JOIN users u
ON u.userid = p.userid
GROUP BY u.userid, u.username;

-- Comments per post
SELECT POSTID, COUNT(*) AS comment_count
FROM COMMENTS
GROUP BY POSTID;

SELECT  c.commentid,p.postid, p.caption, u.userid, u.username, c.commenttext
FROM comments c
INNER JOIN users u ON u.userid = c.userid
INNER JOIN posts p ON p.postid = c.postid;
    


