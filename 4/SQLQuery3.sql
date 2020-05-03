--select * from tblgender
--select * from tblperson
--select * from persontb
--insert into persontb (id,name,genderid,age) values (3, 'mohsin', 1,null)

--alter table tblperson
--add constraint df_tblperson_Gender
--default 3 for Gender
--alter table tblperson 
--drop constraint df_tblperson_Gender
--delete from persontb where ID= 3
alter table persontb
add constraint ck_persontb_age check(age>0 and age <150)