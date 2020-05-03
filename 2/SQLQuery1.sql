alter table tblperson add constraint tblperson_Gender_fk
foreign key (Gender) references tblgender(ID)