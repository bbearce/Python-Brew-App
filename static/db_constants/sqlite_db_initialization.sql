# sqlite

sqlite> .separator ,
sqlite> .import <path>/data.csv <table>

# load thegratefulbrauer db tables
sqlite> .separator
sqlite> .import /Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/fermentables.csv gb_constants_fermentables
sqlite> .import /Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/hops.csv gb_constants_hops
sqlite> .import /Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/styles.csv gb_constants_styles
sqlite> .import /Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/yeast.csv gb_constants_yeast
sqlite> .import /Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/gravity_correction_chart.csv gb_constants_gravity_correction_chart



# postgres
\copy gb_constants_fermentables FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/fermentables.csv' DELIMITER ',' CSV
\copy gb_constants_hops FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/hops.csv' DELIMITER ',' CSV
\copy gb_constants_styles FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/styles.csv' DELIMITER ',' CSV
\copy gb_constants_yeast FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/yeast.csv' DELIMITER ',' CSV
\copy gb_constants_gravity_correction_chart FROM '/Users/bbearce/Documents/Code/Heroku/Python_Brew_App/static/db_constants/gravity_correction_chart.csv' DELIMITER ',' CSV
