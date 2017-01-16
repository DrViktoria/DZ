function validateNamed() {
    var x = document.forms["NewOffice"]["named"].value;

    if (x.length == 0) {
        document.getElementById('id_named').innerHTML = "*укажите название";
        return false;
    } else {
        document.getElementById('id_named').innerHTML = '';
        return true;
    }
}
function validateLocation() {
    var y = document.forms["NewOffice"]["location"].value;
     if(y.length==0){
        document.getElementById('id_location').innerHTML = "*укажите адрес";
        return false;
    } else {
         document.getElementById('id_location').innerHTML='';
         return true;
     }

}

function  validatePhoto() {
     var z = document.forms["NewOffice"]["picture"].value;

     if(z.length==0){
        document.getElementById('id_picture').innerHTML = "*загрузите логотип";
        return false;
    }else{
         document.getElementById('id_picture').innerHTML='';
         return true
     }
}

function validate() {
    if(validateNamed() && validateLocation() && validatePhoto()) return true;
    else return false;

}

