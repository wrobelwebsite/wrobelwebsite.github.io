function init(){
    if(getCookie("pass") == "") document.location="./index.html";
}

//Come on, I'm stupid, but not that stupid.

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

//Encrypted, buddy. Nice try though!

function login(){
    var thing = document.getElementById("pwb").value;
    if(thing == atob("d3JvYmVsQmlvMg==")){
        document.cookie = "pass=true";
        document.location = "./home.html";
    }
    else alert("Incorrect Password, Access Denied.");
}