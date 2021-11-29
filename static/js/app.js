function make_pred(){
    document.getElementById("calcImage").style.display = "block";
    document.getElementById("predicted_price").innerHTML = ""
    document.getElementById("predictLbl").innerHTML = ""
    let carWidth= document.getElementById("car_width").value;
    let carWeight= document.getElementById("car_weight").value;
    let engineSize= document.getElementById("engine_size").value;
    let engineLocation= document.getElementById("engine_location").value;
    let carHeight= document.getElementById("car_height").value;
    let carCompany= document.getElementById("car_company").value;
    fetch("/predictPrice", {
        method: "POST", 
        body: JSON.stringify({
            carWidth: carWidth,
            carWeight: carWeight,
            engineSize: engineSize,
            engineLocation: engineLocation,
            carHeight: carHeight,
            carCompany: carCompany
        }),
        headers:{
            "Content-type":"application/json;charset=UTF-8"

        } 
    }).then(resp=>{
        if (resp.status >= 200 && resp.status <= 299) {
            return resp.json()
        }
        else {
            throw Error(resp.statusText);
        }
        
    }).then(resp=>{
        
        console.log(resp)
        var formatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        });
        setTimeout(function() {
  		//your code to be executed after 1 second
  			document.getElementById("calcImage").style.display = "none";
        	document.getElementById("predicted_price").innerHTML = formatter.format(resp.Prediction)
        	document.getElementById("predictLbl").innerHTML = "Predicted car Price is"
		}, delayInMilliseconds);
        
        
    }).catch((error) => {
    // Handle the error
        console.log(error);
        document.getElementById("predictLbl").innerHTML = "Something went wrong. May be because of this - > " + error
    });
}

var delayInMilliseconds = 2000; //1 second

