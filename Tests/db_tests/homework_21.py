from faker import Faker

fake = Faker()

categories = '''CREATE TABLE public.categories (
    id serial4 PRIMARY KEY,
    name varchar NOT NULL
);'''

products = '''CREATE TABLE public.products (
    id serial4 PRIMARY KEY,
    name varchar,
    descr varchar,
    price numeric(10,2) NOT NULL,
    category_id int,
    CONSTRAINT fk_category
        FOREIGN KEY (category_id)
        REFERENCES public.categories(id)
);'''

INSERT INTO public.categories (name) VALUES ('Electronics');
INSERT INTO public.categories (name) VALUES ('Food');
INSERT INTO public.categories (name) VALUES ('Jewelry');

INSERT INTO public.products (name, descr, price, category_id) VALUES ('iPhone', '16Pro', 50450, 1);
INSERT INTO public.products (name, descr, price, category_id) VALUES ('Bread', 'Brick', 43.5, 2);
INSERT INTO public.products (name, descr, price, category_id) VALUES ('Necklace', 'Gold', 44300, 3);
INSERT INTO public.products (name, descr, price, category_id) VALUES ('iPhone', '12', 22000, 1);

SELECT public.products.name, public.products.descr, public.products.price, public.products.category_id
FROM public.products
INNER JOIN public.categories on public.products.category_id = public.categories.id
WHERE public.categories.name = 'Electronics';