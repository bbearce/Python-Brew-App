
function calc_percent_of_total() {

    // Grab weights and calculate total weight
    var weights = [];
    var total = 0;
    for (i = 1; i < 6; i++) { 
        weights.push(document.getElementsByName('weight_lbs'+String(i))[0].value)
        total += parseFloat(weights[i-1])
    }


    // Calculate the percent of totals for each weight
    var percent_of_totals = [];
    for (var i = 0; i < weights.length; i++) {
        percent_of_totals.push(100*weights[i]/total)
    }

    // Update percent of totals
    for (i = 1; i < 6; i++) { 
        document.getElementById('p_of_total_'+String(i)).innerHTML = String(percent_of_totals[i-1]+" %")
    }

    return total;

}

function calc_og() {

    total_gravity = 0;
    for (var i = 0; i < 5; i++) {
        lbs = $('input[name="weight_lbs'+(i+1).toString()+'"]').val()
        ppg = 1000*(loaded_data['data']['Constants']['gb_constants_fermentables'][i]['ppg'] - 1)
        system_efficiency = Number($('input[name="efficiency"]').val())
        ing_gravtiy = lbs*ppg*system_efficiency

        total_gravity = total_gravity + ing_gravtiy
    }

    return total_gravity/5.5/1000 + 1; //Hook up water another time.
}

function make_chart() {

    total = calc_percent_of_total();

    // Remove previous chart
    var elem = document.getElementById("myChart");
    elem.remove();
    var elem = document.getElementsByClassName("chartjs-size-monitor");
    if(elem.length != 0){
        elem[0].remove();
    }else{console.log('Doesn\'t exists')}
    

    var canvas = document.createElement('canvas');
    canvas.id = 'myChart'
    var div = document.getElementsByClassName("chartDiv")
    div[0].appendChild(canvas)

    // Chart Code
    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
            labels: [document.getElementsByName('ingredient1')[0].value.substring(0,11), 
                     document.getElementsByName('ingredient2')[0].value.substring(0,11),
                     document.getElementsByName('ingredient3')[0].value.substring(0,11),
                     document.getElementsByName('ingredient4')[0].value.substring(0,11),
                     document.getElementsByName('ingredient5')[0].value.substring(0,11)],
            datasets: [{
                label: "My First dataset",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [100*parseInt(document.getElementsByName('weight_lbs1')[0].value)/total,
                       100*parseInt(document.getElementsByName('weight_lbs2')[0].value)/total,
                       100*parseInt(document.getElementsByName('weight_lbs3')[0].value)/total,
                       100*parseInt(document.getElementsByName('weight_lbs4')[0].value)/total,
                       100*parseInt(document.getElementsByName('weight_lbs5')[0].value)/total],
            }]
        },

        // Configuration options go here
        options: {
            scales: {

                xAxes: [{
                  scaleLabel: {
                    display: true,
                    labelString: 'Grain Name'
                  }
                }],

                yAxes: [{
                  scaleLabel: {
                    display: true,
                    labelString: 'Percent of Total (%)'
                  }
                }]
            }    
        }
    });



}



// Display Chart right off the bat
calc_percent_of_total();
make_chart()        

weightsArray = document.getElementsByClassName('fermentables_weight')


//Watch weights to trigger change (PS: we are watching grain name too for labels in graph)
for (var i=0, max=weightsArray.length; i < max; i++) {
    // Do something with the element here
    fermentables = document.getElementsByName('ingredient'+String(i+1))
    fermentables[0].addEventListener("input", function() {
        
        $('input[name="boil_time"]').val(calc_og();
        make_chart();

    });

    weightsArray[i].addEventListener("input", function() {
        
        //calc_percent_of_total();
        make_chart()

    });
}



