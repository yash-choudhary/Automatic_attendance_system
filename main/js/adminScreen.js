var options = {};
var elems = {};
var fs = require('fs')
var config = {
    apiKey: "AIzaSyAlkTeBTBPtnVAaOnNmwiwsFVDIWKhfp5M",
    authDomain: "hackathon-mozofest-2019.firebaseapp.com",
    databaseURL: "https://hackathon-mozofest-2019.firebaseio.com",
    storageBucket: 'gs://hackathon-mozofest-2019.appspot.com/'
};

firebase.initializeApp(config);
var user = firebase.auth().currentUser;

firebase.auth().onAuthStateChanged(function(user) {
    if (user) {
        console.log("Loggd in already : " + user.email);
        M.toast({html:'Welcome back ' + user.email + ' !'});
    }
  });




document.addEventListener('DOMContentLoaded', function() {
    elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
});


$('select').on('change', function() {
    // console.log($(this).val());
    foo($(this).val());
});
var selection;
function foo(selection){
    console.log(selection + " from inside foo along with user : " + user);
        switch(selection){
            case '1': document.location.href = "etc/data1.html";
                    break;
            case '2': document.location.href = "etc/data2.html";
                    break;
            case '3': document.location.href = "etc/data3.html";
                    break;
        }

        //fetch from database
        // Admin signed in.
      
}

function logOut(){
	console.log("Attempting Sign Out");
	firebase.auth().signOut().then(function() {
    	console.log("Sign out successful");
    	document.location.href = "adminLogin.html";
  	}).catch(function(error) {
	    console.log("Error singing out");
  	});
}
function pyCam(){
    
    console.log("Camera Input Running");
    M.toast({html:'Opening Camera Feed'});
    var python = require('child_process').spawn('python', ['py/camcap2.py']);
    python.stdout.on('data',function(data){
        console.log("data: ",data.toString('utf8')+ " from Python ");
        
        sendCSV();
    });

}
function sendCSV(){
    

}

console.log("JS ready");