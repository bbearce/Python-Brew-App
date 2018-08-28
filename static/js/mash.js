function get_mash_info(){
   
    init_grain_temp = parseInt($("input[name='init_grain_temp']")[0].value)
    sacc_rest_temp = parseInt($("input[name='sacc_rest_temp']")[0].value)
    mash_duration = parseInt($("input[name='mash_duration']")[0].value)
    mash_thickness = parseFloat($("input[name='mash_thickness']")[0].value)

    total_grains = calc_percent_of_total()

    mash_volume = total*(mash_thickness/4) // Convert to [Gal] for mash_thickness

    infusion_temp = (0.2/mash_thickness)*(sacc_rest_temp-init_grain_temp)+sacc_rest_temp

    mash_out_volume = ( (170 - sacc_rest_temp)*(0.2*total_grains+mash_volume) ) / (212 - 170)


}

function refresh_mash(){
    
    get_mash_info()

    $("#mash_volume").text(mash_volume)
    $("#infusion_temp").text(infusion_temp)
    $("#mash_out_vol").text(mash_out_volume)

}

// Initialize mash values
get_mash_info()
refresh_mash()

// Things to watch from mash
mash_array = document.getElementsByClassName('mash_input')
for (var i=0, max=mash_array.length; i < max; i++) {
    // Do something with the element here
    mash_array[i].addEventListener("input", function() {
    refresh_mash()

    });

}

// Things to watch from fermentables
for (var i=0, max=5; i < max; i++) {

    fermentables = document.getElementsByName('ingredient'+String(i+1))
    fermentables[0].addEventListener("input", function() {
    refresh_mash()

    });

    weightsArray[i].addEventListener("input", function() {
    refresh_mash()

    });


}
