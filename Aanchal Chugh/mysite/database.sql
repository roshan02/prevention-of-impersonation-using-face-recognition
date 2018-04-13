create table admin_table(adminId int not null, password  not null, centerId int not null, primary key(adminId));
insert into admin_table values(1, "aanchal@123", 1); 
INSERT INTO admin_table VALUES (4, MD5('rutuja'), 4);
create table student(misId int not null, name varchar(50) not null, schoolName varchar(50) not null, schoolId int not null, contact varchar(10) not null, image varchar(20), primary key(misId));
insert into student_table values(111510001, "Aanchal Chugh", "Carmel Academy", 2156, "8888547890", "111510001.jpg");
