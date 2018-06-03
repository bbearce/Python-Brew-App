import psycopg2

conn = psycopg2.connect("dbname='postgres' user='bbearce' host='localhost' password='Alak3_N3van'")
cur = conn.cursor()

recipe = 'initial'
cur.execute("""SELECT * FROM test WHERE recipe = '{}';""".format(recipe))
# cur.execute("""INSERT INTO maybe VALUES('stuff');""")
# cur.execute("""select 5;""")

conn.commit()
cur.close()
conn.close()
# rows = cur.fetchall()
# print(rows)


# interactive:
from models import db
db.create_all()
db.session.commit()
db.drop_all()

import models

# explicit creation
# R = models.Recipe(id=1,recipe='test')

# using SERIAL in postgres to auto generate a sequence
R = models.Recipe(recipe='test')

# commit db session
db.session.add(R)
db.session.commit()

# now query for the current sequence
recipe_id = models.Recipe.query.all()[-1].id

# and add it to the child table's initialization
F = models.Recipe_Fermentables(recipe_id=recipe_id,
                               ingredient='grain1',
                               weight_lbs=13,
                               percent_of_total=100.0)

db.session.add(F)
db.session.commit()

# finally delete a recipe deletes other records
db.session.delete(R)
db.session.commit()

F1 = models.Recipe_Fermentables(id=1, 
                               recipe_id=1, 
                               ingredient='grain1', 
                               weight_lbs=13, 
                               percent_of_total=100.0)
F2 = models.Recipe_Fermentables(id=2, 
                               recipe_id=1, 
                               ingredient='grain2', 
                               weight_lbs=13, 
                               percent_of_total=100.0)

H = models.Recipe_Hops(id=1, 
                       recipe_id=1,
                       name='hop1',
                       weight_oz=1,
                       boil_time_min=60,
                       alpha_acid_content=0.07,
                       utilization=0.70,
                       ibu=30)
M = models.Recipe_Mash(id=1, 
                       recipe_id=1,
                       init_grain_temp=70,
                       infusion_temp=161,
                       sacc_rest_temp=145,
                       mash_duration=90,
                       mash_volume=3.5,
                       mash_thickness=1.25,
                       mash_out_vol=2)
W = models.Recipe_Water(id=1, 
                        recipe_id=1,
                        mash_thickness=1,
                        grain_abs_factor=.25)
Fe = models.Recipe_Fermentation(id=1, 
                                recipe_id=1,
                                days1=5,
                                temp1=70,
                                days2=5,
                                temp2=70,
                                days3=5,
                                temp3=70,
                                days4=5,
                                temp4=70,
                                days5=5,
                                temp5=70)
Y = models.Recipe_Yeast(id=1, 
                        recipe_id=1,
                        name='Safale US-05',
                        attenuation=.80,
                        abv=0.07,
                        og=1.065,
                        fg=1.010,
                        init_cells=1,
                        pitched_cells=1,
                        liters_for_starter=1)
C = models.Recipe_Chemistry(id=1, 
                            recipe_id=1,
                            init_Ca =1,
                            init_Mg =1,
                            init_Na =1,
                            init_Cl =1,
                            init_SO4 =1,
                            init_HCO3_CaCO3 =1,
                            actual_ph =5.4,
                            effective_alkalinity =1,
                            residual_alkalinity =1,
                            ph_down_gypsum_CaSO4 =1,
                            ph_down_cal_chl_CaCl2 =1,
                            ph_down_epsom_salt_MgSO4 =1,
                            ph_up_slaked_lime_CaOH2 =1,
                            ph_up_baking_soda_NaHCO3 =1,
                            ph_up_chalk_CaCO3 =1)
S = models.Recipe_System(id=1, 
                         recipe_id=1,
                         boil_time=60, 
                         evap_rate=0.05, 
                         shrinkage=0.05, 
                         efficiency=0.05, 
                         boil_kettle_dead_space=0.125, 
                         lauter_tun_dead_space=0.125, 
                         mash_tun_dead_space=0.125, 
                         fermentation_tank_loss=0.125)

# single example
db.session.add(R)
db.session.add(S)

db.session.delete(R)
db.session.delete(S)

db.session.commit()

# multiple example
db.session.add_all([R,H,F1,F2,M,W,Fe,Y,C,S])
db.session.commit()




