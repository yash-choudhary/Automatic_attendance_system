var config = {
    apiKey: "AIzaSyAlkTeBTBPtnVAaOnNmwiwsFVDIWKhfp5M",
    authDomain: "hackathon-mozofest-2019.firebaseapp.com",
    databaseURL: "https://hackathon-mozofest-2019.firebaseio.com",
    storageBucket: 'gs://hackathon-mozofest-2019.appspot.com/'
};

firebase.initializeApp(config);
var user = firebase.auth().currentUser;


var database = firebase.database();


var starCountRef = firebase.database().ref('Students');
starCountRef.on('value', function(snapshot) {
	var response = snapshot.val();
    console.log(response);
    document.getElementById(elem1).innerHTML=response.RA1711003010350.RegNo;
}
);