create table product (
product_id serial not null primary key,
name varchar(25) not null,
created_date timestamp not null default now()
);

create table stock (
id serial not null primary key,
product_id integer not null references product(product_id),
quantity integer not null
);

insert into product (name) values ('celular');
insert into product (name) values ('livro');
insert into product (name) values ('tablet');
insert into product (name) values ('notebook');
insert into product (name) values ('roteador');


insert into stock (product_id, quantity) values (1, 5);
insert into stock (product_id, quantity) values (2, 3);
insert into stock (product_id, quantity) values (3, 0);
insert into stock (product_id, quantity) values (4, 1);
insert into stock (product_id, quantity) values (5, 0);


select
    name product_name,
    stock.quantity product_stock
from
    product
inner join 
    stock using (product_id)
group by
    product_name,
    product_stock
order by
    product_stock desc


select sum(quantity) from stock;