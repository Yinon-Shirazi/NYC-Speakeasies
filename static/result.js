function display_results(data, term, foundNames,foundDrinks, foundHoods ){
    $("#placeHolder").empty()

    barsFlag = false;
    drinksFlag = false;
    
    res = ""
    if(foundNames.length == 0 && foundDrinks.length == 0 && foundHoods.length == 0 ){
        $("#resultsNum").append("No results found")
        $("#resultsNum").append("<br>")
        
    }
    else{
        results = foundNames.length + foundDrinks.length + foundHoods.length
        if (results > 1){
            $("#resultsNum").append( results + " results found")
        }
        else{
            $("#resultsNum").append("1 result found")
        }
        
        if(foundNames.length != 0){
            $("#1").append("<ul>")
            for(let i = 0 ; i < foundNames.length; i++){
                res = wrap(foundNames[i]['name'], foundNames[i]["id"])
                $("#1").append(res)
            }
            $("#1").append("</ul>")
            $("#1").append("<br>")
            title = "<div class ='h2'> Bars: </div>"
            $("#1").prepend(title)
            barsFlag = true;
        }

        if(foundDrinks.length != 0){
            if (barsFlag){
                $("#2").append("<ul>")
                for(let i = 0 ; i < foundDrinks.length; i++){
                    item = "<li> <span class = 'results'> <a href = '/view/"+foundDrinks[i][2]+"'> "+foundDrinks[i][0] +"</a> </span>"+"<span class = 'fade_barName'> ("+foundDrinks[i][1]+")" +"</span></li>"
                    $("#2").append(item)
                }
                $("#2").append("</ul>")
                $("#2").append("<br>")
                title = "<div class ='h2'> Drinks: </div>"
                $("#2").prepend(title)
            }
            else{
                $("#1").append("<ul>")
                for(let i = 0 ; i < foundDrinks.length; i++){
                    item = "<li> <span class = 'results'> <a href = '/view/"+foundDrinks[i][2]+"'> "+foundDrinks[i][0] +"</a> </span>"+"<span class = 'fade_barName'> ("+foundDrinks[i][1]+")" +"</span></li>"
                    $("#1").append(item)
                }
                $("#1").append("</ul>")
                $("#1").append("<br>")
                title = "<div class ='h2'> Drinks: </div>"
                $("#1").prepend(title)
            }
            drinksFlag = true;
        }

        if(foundHoods.length != 0){
            if(barsFlag && drinksFlag){
                $("#3").append("<ul>")
                for(let i = 0 ; i < foundHoods.length; i++){
                    item = "<li> <span class = 'results'> <a href = '/view/"+foundHoods[i]["id"]+"'> "+foundHoods[i]["neighborhood"] +"</a> </span>"+"<span class = 'fade_barName'> ("+foundHoods[i]["name"]+")" +"</span></li>"
                    $("#3").append(item)
                }
                res += "</ul>"
                $("#3").append("</ul>")
                $("#3").append("<br>")
                title = "<div class ='h2'> Neighborhoods: </div>"
                $("#3").prepend(title)
            }
            else if (barsFlag || drinksFlag){
                $("#2").append("<ul>")
                for(let i = 0 ; i < foundHoods.length; i++){
                    item = "<li> <span class = 'results'> <a href = '/view/"+foundHoods[i]["id"]+"'> "+foundHoods[i]["neighborhood"] +"</a> </span>"+"<span class = 'fade_barName'> ("+foundHoods[i]["name"]+")" +"</span></li>"
                    $("#2").append(item)
                }
                res += "</ul>"
                $("#2").append("</ul>")
                $("#2").append("<br>")
                title = "<div class ='h2'> Neighborhoods: </div>"
                $("#2").prepend(title)
            }
            else{
                $("#1").append("<ul>")
                for(let i = 0 ; i < foundHoods.length; i++){
                    item = "<li> <span class = 'results'> <a href = '/view/"+foundHoods[i]["id"]+"'> "+foundHoods[i]["neighborhood"] +"</a> </span>"+"<span class = 'fade_barName'> ("+foundHoods[i]["name"]+")" +"</span></li>"
                    $("#1").append(item)
                }
                res += "</ul>"
                $("#1").append("</ul>")
                $("#1").append("<br>")
                title = "<div class ='h2'> Neighborhoods: </div>"
                $("#1").prepend(title)
            }
        }
        
    }
}

function wrap(name, idx){
    return "<li> <span class = 'results'> <a href = '/view/"+idx+"'>"+name +"</a>  </span></li>";
}


$(document).ready(function(){
    display_results(data,term, foundNames, foundDrinks, foundHoods);
    $("#search_input").focus();

})