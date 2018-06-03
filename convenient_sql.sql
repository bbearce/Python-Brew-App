DROP TABLE gb_constants_fermentables;
DROP TABLE gb_constants_gravity_correction_chart;
DROP TABLE gb_constants_hops;
DROP TABLE gb_constants_styles;
DROP TABLE gb_constants_yeast;
DROP TABLE gb_recipe_chemistry;
DROP TABLE gb_recipe_fermentables;
DROP TABLE gb_recipe_fermentation;
DROP TABLE gb_recipe_hops;
DROP TABLE gb_recipe_mash;
DROP TABLE gb_recipe_system;
DROP TABLE gb_recipe_water;
DROP TABLE gb_recipe_yeast;
DROP TABLE gb_recipe_master;
DROP TABLE gb_site_users;
DROP TABLE gb_site_role;


INSERT INTO gb_constants_fermentables;
INSERT INTO gb_constants_gravity_correction_chart;
INSERT INTO gb_constants_hops;
INSERT INTO gb_constants_styles;
INSERT INTO gb_constants_yeast;
INSERT INTO gb_recipe_chemistry;
INSERT INTO gb_recipe_fermentables;
INSERT INTO gb_recipe_fermentation;
INSERT INTO gb_recipe_hops;
INSERT INTO gb_recipe_mash;

INSERT INTO gb_recipe_master(id, recipe)
VALUES (1, 'test');

INSERT INTO gb_recipe_system(recipe_id, boil_time, evap_rate, shrinkage, efficiency, boil_kettle_dead_space, lauter_tun_dead_space, mash_tun_dead_space, fermentation_tank_loss)
VALUES (1,60,0.05,0.05,0.05,0.125,0.125,0.125,0.125);

INSERT INTO gb_recipe_system(recipe_id, boil_time, evap_rate, shrinkage, efficiency, boil_kettle_dead_space, lauter_tun_dead_space, mash_tun_dead_space, fermentation_tank_loss)
VALUES (1,60,0.05,0.05,0.05,0.125,0.125,0.125,0.125);

INSERT INTO gb_recipe_water;
INSERT INTO gb_recipe_yeast;
INSERT INTO gb_recipe_master;
INSERT INTO gb_site_users;
INSERT INTO gb_site_role;












