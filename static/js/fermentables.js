
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

    return total;

}

function calc_og() {

    // Go get the drop down indgredients 
    ingredients = []
    for (var i = 0; i < 5; i++) {
        ingredients.push($('select[name="ingredient'+(i+1).toString()+'"]').val())
    }

    fermentables_properties = []
    for (i in ingredients) {

        var ingredient = ingredients[i]

        // iterate over each element in the array
        
        for (var i = 0; i < Data['Constants']['gb_constants_fermentables'].length; i++){
          // look for the entry with a matching `code` value
          if (Data['Constants']['gb_constants_fermentables'][i].ingredients == ingredient){
             fermentables_properties.push(Data['Constants']['gb_constants_fermentables'][i]['ppg'])
            // obj[i].name is the matched result
          }
        }
    } 


    total_gravity = 0;
    for (var i = 0; i < 5; i++) {
        lbs = $('input[name="weight_lbs'+(i+1).toString()+'"]').val()
        ppg = 1000*(fermentables_properties[i] - 1)
        system_efficiency = Number($('input[name="extraction_efficiency"]').val())/100
        ing_gravtiy = lbs*ppg*system_efficiency

        total_gravity = total_gravity + ing_gravtiy
    }

    return total_gravity/5/1000 + 1; //Hook up water another time.
}

function make_chart() {

    total = calc_percent_of_total();

    // Remove previous chart
    var elem = document.getElementById("fermentablesChart");
    elem.remove();
    var elem = document.getElementsByClassName("chartjs-size-monitor");
    if(elem.length != 0){
        elem[0].remove();
    }else{console.log('Note from fermentables: initial fermentable chart')}
    

    var canvas = document.createElement('canvas');
    canvas.id = 'fermentablesChart'
    var div = document.getElementsByClassName("fermentablesChartDiv")
    div[0].appendChild(canvas)

    // Chart Code
    var ctx = document.getElementById('fermentablesChart').getContext('2d');
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
                label: "Percent of Grain Bill",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [100*parseFloat(document.getElementsByName('weight_lbs1')[0].value)/total,
                       100*parseFloat(document.getElementsByName('weight_lbs2')[0].value)/total,
                       100*parseFloat(document.getElementsByName('weight_lbs3')[0].value)/total,
                       100*parseFloat(document.getElementsByName('weight_lbs4')[0].value)/total,
                       100*parseFloat(document.getElementsByName('weight_lbs5')[0].value)/total],
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

function refresh_fermentables(){
 
    $('#OG').text(calc_og().toFixed(3)); //toFixed() is a rounding method
    make_chart();
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
    refresh_fermentables()

    });

    weightsArray[i].addEventListener("input", function() {
    refresh_fermentables()

    });
}



