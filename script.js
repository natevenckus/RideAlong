

function validate(){
    var username = document.getElementById("uniEmail").value;
    var password = document.getElementById("password").value;
        if(password.length <= 8){
            alert("Please make sure your password is longer than 8 characters");
        }
}