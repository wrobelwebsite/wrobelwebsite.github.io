function init(){
    if(getCookie("pass") == "true") document.location="home.html";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
        for(var i = 0; i <ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function login(){
    var thing = document.getElementById("pwb").value;
    if(thing == "wrobelBio2"){
        document.cookie = "pass=true";
        document.location = "home.html";
    }
    else alert("Incorrect Password, Access Denied.");
}