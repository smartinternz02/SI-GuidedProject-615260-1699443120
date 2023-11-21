function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");

    var block = document.getElementById("warehouse_block");
    var mode = document.getElementById("mode_of_shipment");
    var call = document.getElementById("customer_care_calls");
    var rate = document.getElementById("customer_rating");
    var cost = document.getElementById("cost_of_the_product");
    var prior = document.getElementById("prior_purchases");
    var imp = document.getElementById("product_importance");
    var gender = document.getElementById("gender");
    var dis = document.getElementById("discount_offered");
    var weight = document.getElementById("weight_in_gms");
    var ans = document.getElementById("ans");
  
    var url = "http://127.0.0.1:5000/predict";
  
    $.post(url, {
        block: block,
        mode: mode,
        call: call,
        rate: rate,
        cost, prior, imp, gender, dis, weight
    },function(data, status) {
        console.log(data.ans);
        print(ans);
        ans.innerHTML = data.ans.toString() + " Days</h2>";
        console.log(status);
    });
  }
  
  window.onload = onClickedEstimatePrice;