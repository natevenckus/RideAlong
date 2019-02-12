var loginPopup = document.querySelector("loginPopup");
var loginButton = document.querySelector("login");
var span = document.querySelector("close")[0];

loginButton.onclick = function(){
    console.log("login working")
    loginPopup.display = "block";
}
// span.onclick = function() {
//     loginPopup.style.display = "none";
//   }

// window.onclick = function(event) {
//     console.log("works");
//     if (event.target == loginPopup) {
//         loginPopup.style.display = "none";
//     }
//   }

