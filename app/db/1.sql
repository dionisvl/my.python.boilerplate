CREATE TABLE public.newtable (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"name" varchar NULL
);


INSERT INTO public.newtable ("name") VALUES
	 ('fffff'),
	 ('ddd');
