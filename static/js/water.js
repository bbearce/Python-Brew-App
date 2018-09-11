function get_water_info(){
   
    total_boil_time = parseInt($("input[name='total_boil_time']")[0].value)
    evap_rate = parseFloat($("input[name='evap_rate']")[0].value)
    shrinkage = parseFloat($("input[name='shrinkage']")[0].value)
    
    mash_tun_dead_space = parseFloat($("input[name='mash_tun_dead_space']")[0].value)
    lauter_tun_dead_space = parseFloat($("input[name='lauter_tun_dead_space']")[0].value)
    kettle_dead_space = parseFloat($("input[name='kettle_dead_space']")[0].value)
    fermentation_tank_loss = parseFloat($("input[name='fermentation_tank_loss']")[0].value)
    grain_abs_factor = parseFloat($("input[name='grain_abs_factor']")[0].value)



    get_mash_info()
    // We have these variables after calling get_mash_info
    // total_grains = calc_percent_of_total()
    // mash_volume = total*(mash_thickness/4) // Convert to [Gal] for mash_thickness
    // infusion_temp = (0.2/mash_thickness)*(sacc_rest_temp-init_grain_temp)+sacc_rest_temp
    // mash_out_volume = ( (170 - sacc_rest_temp)*(0.2*total_grains+mash_volume) ) / (212 - 170)

    // [1] Pre-Boil Volume

    

    PBV = ( (batch_size + kettle_dead_space + fermentation_tank_loss)/(1 - shrinkage/100) ) / 
          (1 - ((evap_rate/100)*(total_boil_time/60)))

    // [2] Volume From Runnings

    EL = mash_tun_dead_space + lauter_tun_dead_space // Equipment Loss

    VFR = mash_volume - (total_grains*grain_abs_factor) - EL

    // [3] Sparge Volume

    SV = PBV - VFR

    // [4] Sparge Volume Post Mash Out

    SVPMO = SV - mash_out_volume

    // [5] Total Water Needed

    TW = PBV + (total_grains*grain_abs_factor) + EL


}