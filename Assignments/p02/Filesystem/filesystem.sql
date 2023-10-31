INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(0,'file.txt','FileSystem','32','root','root','rwxr-xr-x','2023-10-26 14:00:00 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(1,'file1.txt','FileSystem','1024','root','root','rwxr-xr-x','2023-10-26 14:05:10 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(2,'file2.txt','FileSystem','1157','root','root','rwxr-xr-x','2023-10-26 14:20:04 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(3,'file3.txt','FileSystem','2304','root','root','rwxr-xr-x','2023-10-26 14:21:00 UTC',NULL,false);
SELECT * from FileSystem;
