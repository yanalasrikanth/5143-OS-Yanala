INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(0,'/','directory','NULL','root','root','rwxr-xr-x','2023-09-13 14:00:00 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(1,'home','directory','NULL','root','root','rwxr-xr-x','2023-11-08 14:00:00 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(1,'home/file.txt','file','32','root','root','rwxr-xr-x','2023-10-26 14:00:00 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(1,'home/file1.txt','file','1024','root','root','rwxr-xr-x','2023-10-26 14:05:10 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(1,'home/file2.txt','file','1157','root','root','rwxr-xr-x','2023-10-26 14:20:04 UTC',NULL,false);
INSERT INTO FileSystem (pid, filename, file_type, file_size, owner,"group", permissions, modification_time, content, hidden)
   VALUES(1,'home/file3.txt','file','2304','root','root','rwxr-xr-x','2023-10-26 14:21:00 UTC',NULL,false);
SELECT * from FileSystem;
