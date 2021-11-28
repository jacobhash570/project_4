function make_pred(){
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
        return resp.json()
    }).then(resp=>{

        console.log(resp)
        var formatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        });
        document.getElementById("predicted_price").innerHTML = formatter.format(resp.Prediction)
        document.getElementById("predictLbl").innerHTML = "Predicted car Price is"
    })
}