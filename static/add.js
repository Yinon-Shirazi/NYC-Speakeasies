
function validateData(){
    $(".warnings").empty()
    empty_msg = "Required Field"
    num_msg = "Please Enter a Numeric Value"
    if(isEmpty($("#name").val())){
        $("#nameWarning").append(empty_msg);
        $("#name").focus();
        return false;
    }
    else if(isEmpty($("#image").val())){
        $(".warnings").empty()
        $("#imageWarning").append(empty_msg);
        $("#image").focus();
        return false;
    }
    else if(isEmpty($("#address").val())){
        $(".warnings").empty()
        $("#addressWarning").append(empty_msg);
        $("#address").focus();
        return false;
    }
    else if(isEmpty($("#about").val())){
        $(".warnings").empty()
        $("#aboutWarning").append(empty_msg);
        $("#about").focus();
        return false;
    }
    else if(isEmpty($("#rating").val())){
        $(".warnings").empty()
        $("#ratingWarning").append(empty_msg);
        $("#rating").focus();
        return false;
    }
    else if(isEmpty($("#price").val())){
        $(".warnings").empty()
        $("#priceWarning").append(empty_msg);
        $("#price").focus();
        return false;
    }
    else if(isEmpty($("#neighborhood").val())){
        $(".warnings").empty()
        $("#hoodWarning").append(empty_msg);
        $("#neighborhood").focus();
        return false;
    }
    else if(isEmpty($("#popular_drinks").val())){
        $(".warnings").empty()
        $("#drinksWarning").append(empty_msg);
        $("#popular_drinks").focus();
        return false;
    }
    else if(isEmpty($("#seating_config").val())){
        $(".warnings").empty()
        $("#seatingWarning").append(empty_msg);
        $("#seating_config").focus();
        return false;
    }
    else{
        $(".warnings").empty()
    }


    if(!$.isNumeric($("#rating").val())){
        $("#ratingWarning").append(num_msg);
        $("#rating").focus();
        return false;
    }
    else if((!$.isNumeric($("#price").val()))){
        $(".warnings").empty()
        $("#priceWarning").append(num_msg);
        $("#price").focus();
        return false;
    }
    else if($("#rating").val() > 5 ||$("#rating").val() <0  ){
        $("#ratingWarning").append("Ratings must be on a 0-5 scale");
        $("#rating").focus();
        return false;
    }
    else{
        $(".warnings").empty()
    }

    return true;

}

function isEmpty(val){
    if (val == ''){
        return true;
    }
    else if($.trim(val) == ''){
        return true;
    }
    return false;
}

function add_bar(){
    newBar = [];
    let name = $("#name").val()
    let new_name = {"name": name}
    newBar.push(new_name); 
    let image = $("#image").val()
    let new_image = {"image": image}
    newBar.push(new_image);
    let address = $("#address").val()
    let new_address = {"address": address}
    newBar.push(new_address);
    let about = $("#about").val()
    let new_about = {"about": name}
    newBar.push(new_about);
    let rating = $("#rating").val()
    let new_rating = {"rating": rating}
    newBar.push(new_rating);
    let price = $("#price").val()
    let new_price = {"price": price}
    newBar.push(new_price);
    let neighborhood = $("#neighborhood").val()
    let new_neighborhood = {"neighborhood": neighborhood}
    newBar.push(new_neighborhood);
    let popular_drinks = $("#popular_drinks").val()
    let new_popular_drinks = {"popular_drinks": popular_drinks}
    newBar.push(new_popular_drinks);
    let seating_config = $("#seating_config").val()
    let new_seating_config = {"seating_config": seating_config} 
    newBar.push(new_seating_config);   

    $.ajax({
        type: "POST",
        url: "add_bar",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(newBar),
        success: function(result){
            let id = result["data"]
            confirm(name, id)
            $(".add").val("")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function confirm(name, id){
    msg = "The new bar " +name + " has been succesfully created."
    btn = '<a href="/view/'+id+'" class="btn view buttn" style="position: static" >See Profile</a>'
    $("#success").append("<span class = 'check'>&#10003;</span>")
    $("#success").append(msg)
    $("#success").append(btn)

}


$(document).ready(function(){
    $("#success").empty()
    $("warnings").empty()
    
    $("#send").click(function(){
        if(validateData()){
            add_bar()
        }
    })


})