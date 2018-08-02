console.log('hello world')
$(function() {
$('#load').bind('click', function() {

  // Go to load in python and pass in the recipe input value
  $.getJSON($SCRIPT_ROOT + '/load', {
    recipe: $('input[name="recipe"]').val(),

  // the load() function returns a json object with key value pairs
  }, function(data) {
    x = data
    /*
    if (data['recipe'] == "that recipe exists already"){
    
    // If this recipe doesn't exist in the database then tell the user.

    $('#messages').text("That recipe doesn't exist")

    } else {
    // If this recipe exists in the database then tell the user and load it.

    $('#messages').text("You have loaded recipe "+data['recipe'])

    // Recipe
    $('select[name="style"]').val(data['style'])

    // System
    $('input[name="boil_time"]').val(data['boil_time'])
    $('input[name="evap_rate"]').val(data['evap_rate'])
    $('input[name="shrinkage"]').val(data['shrinkage'])
    $('input[name="efficiency"]').val(data['efficiency'])
    $('input[name="boil_kettle_dead_space"]').val(data['boil_kettle_dead_space'])
    $('input[name="lauter_tun_dead_space"]').val(data['lauter_tun_dead_space'])
    $('input[name="mash_tun_dead_space"]').val(data['mash_tun_dead_space'])
    $('input[name="fermentation_tank_loss"]').val(data['fermentation_tank_loss'])

    // Fermentables
    $('select[name="ingredient1"]').val(data['ingredient1'])
    $('input[name="weight_lbs1"]').val(data['weight_lbs1'])
    $('input[name="percent_of_total1"]').val(data['percent_of_total1'])

    $('select[name="ingredient2"]').val(data['ingredient2'])
    $('input[name="weight_lbs2"]').val(data['weight_lbs2'])
    $('input[name="percent_of_total2"]').val(data['percent_of_total2'])

    $('select[name="ingredient3"]').val(data['ingredient3'])
    $('input[name="weight_lbs3"]').val(data['weight_lbs3'])
    $('input[name="percent_of_total3"]').val(data['percent_of_total3'])

    $('select[name="ingredient4"]').val(data['ingredient4'])
    $('input[name="weight_lbs4"]').val(data['weight_lbs4'])
    $('input[name="percent_of_total4"]').val(data['percent_of_total4'])

    $('select[name="ingredient5"]').val(data['ingredient5'])
    $('input[name="weight_lbs5"]').val(data['weight_lbs5'])
    $('input[name="percent_of_total5"]').val(data['percent_of_total5'])

    // Hops
    $('select[name="hop1"]').val(data['hop1'])
    $('input[name="weight_oz1"]').val(data['weight_oz1'])
    $('input[name="boil_time_min1"]').val(data['boil_time_min1'])
    $('input[name="alpha_acid_content1"]').val(data['alpha_acid_content1'])
    $('input[name="utilization1"]').val(data['utilization1'])
    $('input[name="ibu1"]').val(data['ibu1'])

    $('select[name="hop2"]').val(data['hop2'])
    $('input[name="weight_oz2"]').val(data['weight_oz2'])
    $('input[name="boil_time_min2"]').val(data['boil_time_min2'])
    $('input[name="alpha_acid_content2"]').val(data['alpha_acid_content2'])
    $('input[name="utilization2"]').val(data['utilization2'])
    $('input[name="ibu2"]').val(data['ibu2'])

    $('select[name="hop3"]').val(data['hop3'])
    $('input[name="weight_oz3"]').val(data['weight_oz3'])
    $('input[name="boil_time_min3"]').val(data['boil_time_min3'])
    $('input[name="alpha_acid_content3"]').val(data['alpha_acid_content3'])
    $('input[name="utilization3"]').val(data['utilization3'])
    $('input[name="ibu3"]').val(data['ibu3'])

    // Mash
    $('input[name="init_grain_temp"]').val(data['init_grain_temp'])
    $('input[name="infusion_temp"]').val(data['infusion_temp'])
    $('input[name="sacc_rest_temp"]').val(data['sacc_rest_temp'])
    $('input[name="mash_duration"]').val(data['mash_duration'])
    $('input[name="mash_volume"]').val(data['mash_volume'])
    $('input[name="mash_thickness"]').val(data['mash_thickness'])
    $('input[name="mash_out_vol"]').val(data['mash_out_vol'])

    // Yeast
    $('select[name="yeast_name"]').val(data['yeast_name'])
    $('input[name="attenuation"]').val(data['attenuation'])
    $('input[name="abv"]').val(data['abv'])
    $('input[name="og"]').val(data['og'])
    $('input[name="fg"]').val(data['fg'])
    $('input[name="init_cells"]').val(data['init_cells'])
    $('input[name="pitched_cells"]').val(data['pitched_cells'])
    $('input[name="liters_for_starter"]').val(data['liters_for_starter'])

    // Water
    $('input[name="grain_abs_factor"]').val(data['grain_abs_factor'])

    // Fermentation
    $('input[name="days1"]').val(data['days1'])
    $('input[name="temp1"]').val(data['temp1'])
    $('input[name="days2"]').val(data['days2'])
    $('input[name="temp2"]').val(data['temp2'])
    $('input[name="days3"]').val(data['days3'])
    $('input[name="temp3"]').val(data['temp3'])
    $('input[name="days4"]').val(data['days4'])
    $('input[name="temp4"]').val(data['temp4'])
    $('input[name="days5"]').val(data['days5'])
    $('input[name="temp5"]').val(data['temp5'])

    // Chemistry
    $('input[name="init_Ca"]').val(data['init_Ca'])
    $('input[name="init_Mg"]').val(data['init_Mg'])
    $('input[name="init_Na"]').val(data['init_Na'])
    $('input[name="init_Cl"]').val(data['init_Cl'])
    $('input[name="init_SO4"]').val(data['init_SO4'])
    $('input[name="init_HCO3_CaCO3"]').val(data['init_HCO3_CaCO3'])
    $('input[name="actual_ph"]').val(data['actual_ph'])
    $('input[name="effective_alkalinity"]').val(data['effective_alkalinity'])
    $('input[name="residual_alkalinity"]').val(data['residual_alkalinity'])
    $('input[name="ph_down_gypsum_CaSO4"]').val(data['ph_down_gypsum_CaSO4'])
    $('input[name="ph_down_cal_chl_CaCl2"]').val(data['ph_down_cal_chl_CaCl2'])
    $('input[name="ph_down_epsom_salt_MgSO4"]').val(data['ph_down_epsom_salt_MgSO4'])
    $('input[name="ph_up_slaked_lime_CaOH2"]').val(data['ph_up_slaked_lime_CaOH2'])
    $('input[name="ph_up_baking_soda_NaHCO3"]').val(data['ph_up_baking_soda_NaHCO3'])
    $('input[name="ph_up_chalk_CaCO3"]').val(data['ph_up_chalk_CaCO3'])


    // Rerun app calculations
    //calc_percent_of_total();
    //make_chart();
    // App Area
    $('#app').text(data['recipe'])
    
    
    }

    */
    

  });
  return false;
});
});