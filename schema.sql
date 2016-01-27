DROP TABLE merchandises;
CREATE TABLE merchandises (
merchandise_id varchar(32),
merchandise_name text
);

DROP TABLE makeups;
CREATE TABLE makeups (
merchandise_id varchar(32),
category_id varchar(32),
category_name text
);

DROP TABLE brands;
CREATE TABLE brands (
category_id varchar(32),
brand_id varchar(32),
brand_name text
);

DROP TABLE products_brand;
CREATE TABLE products_brand (
brand_id varchar(32),
product_id varchar(32),
product_name text
);

DROP TABLE products_category;
CREATE TABLE products_category (
category_id varchar(32),
product_id varchar(32),
product_name text
);

DROP TABLE products_details;
CREATE TABLE products_details (
product_id varchar(32),
product_desc text,
product_price integer,
product_in_stock integer
);
