SELECT users.first_name, users.last_name, user2.first_name,user2.last_name FROM users 
 JOIN friendships ON users.id= friendships.users_id 
 JOIN users as user2 ON user2.id = friendships.friend_id;

select * from friendships;

select * from users;

INSERT INTO friendships (users_id,friend_id)
VALUES(3,2);

