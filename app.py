from flask import Flask, flash, jsonify, render_template, request, redirect, url_for
from flask_script import Manager
import psycopg2

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://bbearce:Alak3_N3van@localhost/gratefulbrauer"

from models import db  # <-- this needs to be placed after app is created

manager = Manager(app)


@app.route('/load')
def load():

    recipe = request.args.get('recipe', 0, type=str)

    import models

    # Recipe = models.Recipe(recipe=recipe)
    Recipe = models.Recipe.query.filter_by(recipe = recipe).first()
    recipe_id = Recipe.id

    System = models.Recipe_System.query.filter_by(recipe_id = recipe_id).first()
    Fermentables = models.Recipe_Fermentables.query.filter_by(recipe_id = recipe_id).all()
    Hops = models.Recipe_Hops.query.filter_by(recipe_id = recipe_id).all()
    Mash = models.Recipe_Mash.query.filter_by(recipe_id = recipe_id).first()
    Yeast = models.Recipe_Yeast.query.filter_by(recipe_id = recipe_id).first()
    Water = models.Recipe_Water.query.filter_by(recipe_id = recipe_id).first()
    Fermentation = models.Recipe_Fermentation.query.filter_by(recipe_id = recipe_id).first()
    Chemistry = models.Recipe_Chemistry.query.filter_by(recipe_id = recipe_id).first()



    # Database stuff
    # conn = psycopg2.connect("dbname='gratefulbrauer' user='bbearce' host='localhost' password='Alak3_N3van'")
    # cur = conn.cursor()
    # cur.execute("""SELECT * FROM test WHERE recipe = '{}';""".format(recipe))
    # recipe_data = cur.fetchone()

    # conn.commit()
    # cur.close()
    # conn.close()
    # # rows = cur.fetchall()
    # print("""SELECT * FROM test WHERE recipe = '{}';""".format(recipe))

    # return jsonify(result='{{"a": [{a}]}}'.format(a))
    return jsonify(recipe=recipe, 
                   # System
                   boil_time=System.boil_time,
                   evap_rate=System.evap_rate,
                   shrinkage=System.shrinkage,
                   efficiency=System.efficiency,
                   boil_kettle_dead_space=System.boil_kettle_dead_space,
                   lauter_tun_dead_space=System.lauter_tun_dead_space,
                   mash_tun_dead_space=System.mash_tun_dead_space,
                   fermentation_tank_loss=System.fermentation_tank_loss,
                   # Fermentables
                   ingredient1=Fermentables[0].ingredient,
                   weight_lbs1=Fermentables[0].weight_lbs,
                   percent_of_total1=Fermentables[0].percent_of_total,
                   ingredient2=Fermentables[1].ingredient,
                   weight_lbs2=Fermentables[1].weight_lbs,
                   percent_of_total2=Fermentables[1].percent_of_total,
                   ingredient3=Fermentables[2].ingredient,
                   weight_lbs3=Fermentables[2].weight_lbs,
                   percent_of_total3=Fermentables[2].percent_of_total,
                   ingredient4=Fermentables[3].ingredient,
                   weight_lbs4=Fermentables[3].weight_lbs,
                   percent_of_total4=Fermentables[3].percent_of_total,
                   ingredient5=Fermentables[4].ingredient,
                   weight_lbs5=Fermentables[4].weight_lbs,
                   percent_of_total5=Fermentables[4].percent_of_total,
                   # Hops
                   hop1=Hops[0].hop_name,
                   weight_oz1=Hops[0].weight_oz,
                   boil_time_min1=Hops[0].boil_time_min,
                   alpha_acid_content1=Hops[0].alpha_acid_content,
                   utilization1=Hops[0].utilization,
                   ibu1=Hops[0].ibu,
                   hop2=Hops[1].hop_name,
                   weight_oz2=Hops[1].weight_oz,
                   boil_time_min2=Hops[1].boil_time_min,
                   alpha_acid_content2=Hops[1].alpha_acid_content,
                   utilization2=Hops[1].utilization,
                   ibu2=Hops[1].ibu,
                   hop3=Hops[2].hop_name,
                   weight_oz3=Hops[2].weight_oz,
                   boil_time_min3=Hops[2].boil_time_min,
                   alpha_acid_content3=Hops[2].alpha_acid_content,
                   utilization3=Hops[2].utilization,
                   ibu3=Hops[2].ibu,
                   # Mash
                   init_grain_temp=Mash.init_grain_temp,
                   infusion_temp=Mash.infusion_temp,
                   sacc_rest_temp=Mash.sacc_rest_temp,
                   mash_duration=Mash.mash_duration,
                   mash_volume=Mash.mash_volume,
                   mash_thickness=Mash.mash_thickness,
                   mash_out_vol=Mash.mash_out_vol,
                   # Yeast
                   yeast_name=Yeast.yeast_name,
                   attenuation=Yeast.attenuation,
                   abv=Yeast.abv,
                   og=Yeast.og,
                   fg=Yeast.fg,
                   init_cells=Yeast.init_cells,
                   pitched_cells=Yeast.pitched_cells,
                   liters_for_starter=Yeast.liters_for_starter,
                   # Water
                   grain_abs_factor=Water.grain_abs_factor,
                   # Fermentation
                   days1=Fermentation.days1,
                   temp1=Fermentation.temp1,
                   days2=Fermentation.days2,
                   temp2=Fermentation.temp2,
                   days3=Fermentation.days3,
                   temp3=Fermentation.temp3,
                   days4=Fermentation.days4,
                   temp4=Fermentation.temp4,
                   days5=Fermentation.days5,
                   temp5=Fermentation.temp5,
                   # Chemistry
                   init_Ca=Chemistry.init_Ca,
                   init_Mg=Chemistry.init_Mg,
                   init_Na=Chemistry.init_Na,
                   init_Cl=Chemistry.init_Cl,
                   init_SO4=Chemistry.init_SO4,
                   init_HCO3_CaCO3=Chemistry.init_HCO3_CaCO3,
                   actual_ph=Chemistry.actual_ph,
                   effective_alkalinity=Chemistry.effective_alkalinity,
                   residual_alkalinity=Chemistry.residual_alkalinity,
                   ph_down_gypsum_CaSO4=Chemistry.ph_down_gypsum_CaSO4,
                   ph_down_cal_chl_CaCl2=Chemistry.ph_down_cal_chl_CaCl2,
                   ph_down_epsom_salt_MgSO4=Chemistry.ph_down_epsom_salt_MgSO4,
                   ph_up_slaked_lime_CaOH2=Chemistry.ph_up_slaked_lime_CaOH2,
                   ph_up_baking_soda_NaHCO3=Chemistry.ph_up_baking_soda_NaHCO3,
                   ph_up_chalk_CaCO3=Chemistry.ph_up_chalk_CaCO3
                   )

@app.route('/save')
def save():
    flash('Saved')
    # Common to all
    recipe = request.args.get('recipe', 0, type=str)

    # Database table: gb_recipe_system
    # recipe
    boil_time = request.args.get('boil_time', 0, type=str)
    evap_rate = request.args.get('evap_rate', 0, type=str)
    shrinkage = request.args.get('shrinkage', 0, type=str)
    efficiency = request.args.get('efficiency', 0, type=str)
    boil_kettle_dead_space = request.args.get('boil_kettle_dead_space', 0, type=str)
    lauter_tun_dead_space = request.args.get('lauter_tun_dead_space', 0, type=str)
    mash_tun_dead_space = request.args.get('mash_tun_dead_space', 0, type=str)
    fermentation_tank_loss = request.args.get('fermentation_tank_loss', 0, type=str)
    
    # Database table: gb_recipe_fermentables
    # recipe
    ingredient1 = request.args.get('ingredient1', 0, type=str)
    weight_lbs1 = request.args.get('weight_lbs1', 0, type=str)
    percent_of_total1 = request.args.get('percent_of_total1', 0, type=str)

    ingredient2 = request.args.get('ingredient2', 0, type=str)
    weight_lbs2 = request.args.get('weight_lbs2', 0, type=str)
    percent_of_total2 = request.args.get('percent_of_total2', 0, type=str)

    ingredient3 = request.args.get('ingredient3', 0, type=str)
    weight_lbs3 = request.args.get('weight_lbs3', 0, type=str)
    percent_of_total3 = request.args.get('percent_of_total3', 0, type=str)

    ingredient4 = request.args.get('ingredient4', 0, type=str)
    weight_lbs4 = request.args.get('weight_lbs4', 0, type=str)
    percent_of_total4 = request.args.get('percent_of_total4', 0, type=str)

    ingredient5 = request.args.get('ingredient5', 0, type=str)
    weight_lbs5 = request.args.get('weight_lbs5', 0, type=str)
    percent_of_total5 = request.args.get('percent_of_total5', 0, type=str)

    # Database table: gb_recipe_hops
    # recipe
    hop1 = request.args.get('hop1', 0, type=str)    
    weight_oz1 = request.args.get('weight_oz1', 0, type=str)    
    boil_time_min1 = request.args.get('boil_time_min1', 0, type=str)    
    alpha_acid_content1 = request.args.get('alpha_acid_content1', 0, type=str)    
    utilization1= request.args.get('utilization1', 0, type=str)    
    ibu1 = request.args.get('ibu1', 0, type=str)

    hop2 = request.args.get('hop2', 0, type=str)    
    weight_oz2 = request.args.get('weight_oz2', 0, type=str)    
    boil_time_min2 = request.args.get('boil_time_min2', 0, type=str)    
    alpha_acid_content2 = request.args.get('alpha_acid_content2', 0, type=str)    
    utilization2= request.args.get('utilization2', 0, type=str)    
    ibu2 = request.args.get('ibu2', 0, type=str)

    hop3 = request.args.get('hop3', 0, type=str)    
    weight_oz3 = request.args.get('weight_oz3', 0, type=str)    
    boil_time_min3 = request.args.get('boil_time_min3', 0, type=str)    
    alpha_acid_content3 = request.args.get('alpha_acid_content3', 0, type=str)    
    utilization3= request.args.get('utilization3', 0, type=str)    
    ibu3 = request.args.get('ibu3', 0, type=str)    

    # Database table: gb_recipe_mash
    # recipe
    init_grain_temp = request.args.get('init_grain_temp', 0, type=str)
    infusion_temp = request.args.get('infusion_temp', 0, type=str)
    sacc_rest_temp = request.args.get('sacc_rest_temp', 0, type=str)
    mash_duration = request.args.get('mash_duration', 0, type=str)
    mash_volume = request.args.get('mash_volume', 0, type=str)
    mash_thickness = request.args.get('mash_thickness', 0, type=str)
    mash_out_vol = request.args.get('mash_out_vol', 0, type=str)

    # Database table: gb_recipe_yeast
    # recipe
    yeast_name = request.args.get('yeast_name', 0, type=str)
    attenuation = request.args.get('attenuation', 0, type=str)
    abv = request.args.get('abv', 0, type=str)
    og = request.args.get('og', 0, type=str)
    fg = request.args.get('fg', 0, type=str)
    init_cells = request.args.get('init_cells', 0, type=str)
    pitched_cells = request.args.get('pitched_cells', 0, type=str)
    liters_for_starter = request.args.get('liters_for_starter', 0, type=str)

    # Database table: gb_recipe_water
    # recipe
    grain_abs_factor = request.args.get('grain_abs_factor', 0, type=str)

    # Database table: gb_recipe_fermentation
    # recipe
    days1 = request.args.get('days1', 0, type=str)
    temp1 = request.args.get('temp1', 0, type=str)
    days2 = request.args.get('days2', 0, type=str)
    temp2 = request.args.get('temp2', 0, type=str)
    days3 = request.args.get('days3', 0, type=str)
    temp3 = request.args.get('temp3', 0, type=str)
    days4 = request.args.get('days4', 0, type=str)
    temp4 = request.args.get('temp4', 0, type=str)
    days5 = request.args.get('days5', 0, type=str)
    temp5 = request.args.get('temp5', 0, type=str)

    # Database table: gb_recipe_chemistry
    # recipe
    init_Ca = request.args.get('init_Ca', 0, type=str)
    init_Mg = request.args.get('init_Mg', 0, type=str)
    init_Na = request.args.get('init_Na', 0, type=str)
    init_Cl = request.args.get('init_Cl', 0, type=str)
    init_SO4 = request.args.get('init_SO4', 0, type=str)
    init_HCO3_CaCO3 = request.args.get('init_HCO3_CaCO3', 0, type=str)
    actual_ph = request.args.get('actual_ph', 0, type=str)
    effective_alkalinity = request.args.get('effective_alkalinity', 0, type=str)
    residual_alkalinity = request.args.get('residual_alkalinity', 0, type=str)
    ph_down_gypsum_CaSO4 = request.args.get('ph_down_gypsum_CaSO4', 0, type=str)
    ph_down_cal_chl_CaCl2 = request.args.get('ph_down_cal_chl_CaCl2', 0, type=str)
    ph_down_epsom_salt_MgSO4 = request.args.get('ph_down_epsom_salt_MgSO4', 0, type=str)
    ph_up_slaked_lime_CaOH2 = request.args.get('ph_up_slaked_lime_CaOH2', 0, type=str)
    ph_up_baking_soda_NaHCO3 = request.args.get('ph_up_baking_soda_NaHCO3', 0, type=str)
    ph_up_chalk_CaCO3 = request.args.get('ph_up_chalk_CaCO3', 0, type=str)

    import models

    Recipe = models.Recipe(recipe=recipe)

    db.session.add(Recipe)
    db.session.commit()

    recipe_id = models.Recipe.query.all()[-1].id

    System = models.Recipe_System(recipe_id=recipe_id,
                             boil_time=boil_time, 
                             evap_rate=evap_rate, 
                             shrinkage=shrinkage, 
                             efficiency=efficiency, 
                             boil_kettle_dead_space=boil_kettle_dead_space, 
                             lauter_tun_dead_space=lauter_tun_dead_space, 
                             mash_tun_dead_space=mash_tun_dead_space, 
                             fermentation_tank_loss=fermentation_tank_loss)
    
    Fermentables1 = models.Recipe_Fermentables(recipe_id=recipe_id,
                                   ingredient=ingredient1,
                                   weight_lbs=weight_lbs1,
                                   percent_of_total=percent_of_total1)
    Fermentables2 = models.Recipe_Fermentables(recipe_id=recipe_id,
                                   ingredient=ingredient2,
                                   weight_lbs=weight_lbs2,
                                   percent_of_total=percent_of_total2)
    Fermentables3 = models.Recipe_Fermentables(recipe_id=recipe_id,
                                   ingredient=ingredient3,
                                   weight_lbs=weight_lbs3,
                                   percent_of_total=percent_of_total3)
    Fermentables4 = models.Recipe_Fermentables(recipe_id=recipe_id,
                                   ingredient=ingredient4,
                                   weight_lbs=weight_lbs4,
                                   percent_of_total=percent_of_total4)
    Fermentables5 = models.Recipe_Fermentables(recipe_id=recipe_id,
                                   ingredient=ingredient5,
                                   weight_lbs=weight_lbs5,
                                   percent_of_total=percent_of_total5)

    Hops1 = models.Recipe_Hops(recipe_id=recipe_id,
                       hop_name=hop1,
                       weight_oz=weight_oz1,
                       boil_time_min=boil_time_min1,
                       alpha_acid_content=alpha_acid_content1,
                       utilization=utilization1,
                       ibu=ibu1)

    Hops2 = models.Recipe_Hops(recipe_id=recipe_id,
                       hop_name=hop2,
                       weight_oz=weight_oz2,
                       boil_time_min=boil_time_min2,
                       alpha_acid_content=alpha_acid_content2,
                       utilization=utilization2,
                       ibu=ibu2)

    Hops3 = models.Recipe_Hops(recipe_id=recipe_id,
                       hop_name=hop3,
                       weight_oz=weight_oz3,
                       boil_time_min=boil_time_min3,
                       alpha_acid_content=alpha_acid_content3,
                       utilization=utilization3,
                       ibu=ibu3)


    Mash = models.Recipe_Mash(recipe_id=recipe_id,
                           init_grain_temp=init_grain_temp,
                           infusion_temp=infusion_temp,
                           sacc_rest_temp=sacc_rest_temp,
                           mash_duration=mash_duration,
                           mash_volume=mash_volume,
                           mash_thickness=mash_thickness,
                           mash_out_vol=mash_out_vol)
    
    Yeast = models.Recipe_Yeast(recipe_id=recipe_id,
                            yeast_name=yeast_name,
                            attenuation=attenuation,
                            abv=abv,
                            og=og,
                            fg=fg,
                            init_cells=init_cells,
                            pitched_cells=pitched_cells,
                            liters_for_starter=liters_for_starter)

    Water = models.Recipe_Water(recipe_id=recipe_id,
                            grain_abs_factor=.25)
    Fermentation = models.Recipe_Fermentation(recipe_id=recipe_id,
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
    
    Chemistry = models.Recipe_Chemistry(recipe_id=recipe_id,
                                init_Ca =init_Ca,
                                init_Mg =init_Mg,
                                init_Na =init_Na,
                                init_Cl =init_Cl,
                                init_SO4 =init_SO4,
                                init_HCO3_CaCO3 =init_HCO3_CaCO3,
                                actual_ph =actual_ph,
                                effective_alkalinity =effective_alkalinity,
                                residual_alkalinity =residual_alkalinity,
                                ph_down_gypsum_CaSO4 =ph_down_gypsum_CaSO4,
                                ph_down_cal_chl_CaCl2 =ph_down_cal_chl_CaCl2,
                                ph_down_epsom_salt_MgSO4 =ph_down_epsom_salt_MgSO4,
                                ph_up_slaked_lime_CaOH2 =ph_up_slaked_lime_CaOH2,
                                ph_up_baking_soda_NaHCO3 =ph_up_baking_soda_NaHCO3,
                                ph_up_chalk_CaCO3 =ph_up_chalk_CaCO3)

    

    Fermentables = [Fermentables1, Fermentables2, Fermentables3, Fermentables4, Fermentables5]

    Hops = [Hops1, Hops2, Hops3]

    db.session.add_all(Fermentables + Hops + [Mash, Water, Fermentation, Yeast, Chemistry, System])
    db.session.commit()


    # Database stuff 1
    # conn = psycopg2.connect("dbname='gratefulbrauer' user='bbearce' host='localhost' password='Alak3_N3van'")
    # cur = conn.cursor()
    # cur.execute("""
    #     INSERT INTO gb_recipe_system(recipe, boil_time, evap_rate, shrinkage, efficiency, boil_kettle_dead_space_gal, lauter_tun_dead_space_gal, mash_tun_dead_space_gal, fermentation_tank_loss_gal)
    #     VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}');
    #     """.format(recipe, boil_time, evap_rate, shrinkage, efficiency, boil_kettle_dead_space, lauter_tun_dead_space, mash_tun_dead_space, fermentation_tank_loss))

    # conn.commit()
    # cur.close()
    # conn.close()
    # rows = cur.fetchall()
    
    # return jsonify(result='{{"a": [{a}]}}'.format(a))
    return jsonify(value=recipe)

@app.route('/delete')
def delete():
    
    import models

    # Common to all
    recipe = request.args.get('recipe', 0, type=str)

    Recipe = models.Recipe.query.filter_by(recipe=recipe).all()[0]

    db.session.delete(Recipe)
    db.session.commit()

    flash('Deleted')
    return jsonify(value=recipe)
    #return render_template('index.html')
    



@app.route('/')
def index():
    flash('Hit Index')
    return render_template('index.html')

if __name__ == "__main__":
    manager.run()
    # app.run(debug=True)



































