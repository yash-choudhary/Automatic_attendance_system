// Initialize Firebase

    var config = {
        apiKey: "AIzaSyAlkTeBTBPtnVAaOnNmwiwsFVDIWKhfp5M",
        authDomain: "hackathon-mozofest-2019.firebaseapp.com",
        databaseURL: "https://hackathon-mozofest-2019.firebaseio.com",
        projectId: "hackathon-mozofest-2019",
        storageBucket: "hackathon-mozofest-2019.appspot.com",
        messagingSenderId: "835193922935"
    };
    firebase.initializeApp(config);
    //clear any signed in users.....
    firebase.auth().signOut().then(function() {
        console.log("Sign out successful");
      }).catch(function(error) {
        console.log("Error singing out");
      });

    function foo(){
        
        console.log("working on FOO");
        var email = document.getElementById("loginemail").value;
        var password = document.getElementById("loginpassword").value;
        
        firebase.auth().signInWithEmailAndPassword(email,password).catch(function(error) {  //catch errors if any
                console.log(error);
            }).then(function(){                                     //when login is complete, only then.....
                var user = firebase.auth().currentUser;
                if(user!=null){
                    console.log("Faculty Login Success");
                    document.location.href = "dataEntry.html";
                }
                else{
                    console.log("Login Unsuccessful");
                    M.toast({html: 'Invalid credentials! Please try again!'});
                }
        });
        console.log("outside");

    }