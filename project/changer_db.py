# import sqlite3

# base = sqlite3.connect('project/db.sqlite3')
# cur = base.cursor()

# base.execute('CREATE TABLE IF NOT EXISTS "main_menu" ("id" INTEGER PRIMARY KEY AUTOINCREMENT, "title" varchar(50) NOT NULL, "item" varchar(50) NOT NULL, "alergian" varchar(50) NOT NULL, "price" varchar(50) NOT NULL, "description" text NOT NULL)')
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'Margherita Pizza', '1, 3, 7', '€8.00 €10.00', 'None'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'Ham Pizza', '1, 2, 3, 7', '€9.00 €11.00', 'None'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'Hawaiian Pizza', '1, 2, 3, 7', '€10.00 €12.00', 'Ham mushroom and pineapple'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'Pepperoni', '1, 3, 7', '€9.80 €11.80', 'None'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'Meat Feast Pizza', '1, 3, 7, 9', '€10.20 €13.20', 'Ham, pepperoni and chicken'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'Vegetarian Pizza', '1, 3, 7', '€10.50 €13.50', 'Mushrooms, onions, olives, peppers, sweetcorn, pineapple'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'Kebab Pizza', '1, 3, 7', '€10.50 €12.80', 'Lamb doner or chicken doner, onion and peppers'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas', 'House Special Pizza', '1, 3, 7', '€11.00 €12.80', 'Ham, pepperoni, mushroom, onion, green pepper, sweetcorn, pineapple'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ('Pizzas Meal', 'Pizza Meal', 'None', '€11.00 €14.60', 'None'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ( 'Pizzas Meal', 'Create your own Pizza', 'None', 'Any Toppings €1.00', 'Meal including chips and drinks'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ( 'Pizzas Meal', 'Pizza Deal', 'None', '€23.00', '12" Pizza, 3 goujons, garlic bread with cheese, 2 chips, 1 sauce of your choice and large drink'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ( 'Pizzas Meal', 'Garlic Bread with Cheese', '3, 7', '€5.00', 'None'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ( 'Pizzas Meal', 'Garlic Bread', '3, 7', '€4.50', 'None'))
# base.commit()
# cur.execute("""INSERT INTO "main_menu" ("title", "item", "alergian", "price", "description") VALUES (?, ?, ?, ?, ?)""", ( 'Pizzas Meal', 'Naan Bread', '3, 7', '€2.00', 'None'))
# base.commit()
