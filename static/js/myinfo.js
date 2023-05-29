
var pw = false;
var npw = false;
var cnpw = false;

function capLock(e){
    kc = e.keyCode ? e.keyCode : e.which;
    sk = e.shiftKey ? e.shiftKey : ((kc == 16) ? true : false);
    if(((kc >= 65 && kc <= 90) && !sk)||((kc >= 97 && kc <= 122) && sk)){
        document.getElementById('divMayus3').style.display="none";
        document.getElementById('divMayus').style.display = 'block';
        document.getElementById('divMayus2').style.display = 'block';
        document.getElementById('divMayus4').style.display = 'block';
    }
    else{
        document.getElementById('divMayus').style.display="none";
        document.getElementById('divMayus2').style.display = "none";
        document.getElementById('divMayus4').style.display = "none";
        document.getElementById('divMayus3').style.display = 'block';
    }
}

function p_check(password){
    var pattern = /^(?=.*?[a-zA-Z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/g;

    var value = document.getElementById(password).value;

    if (pattern.test(value)){
        document.getElementById(password).style.color = "green";
        document.getElementById(password).style.borderColor = "green";
        if(password == 'password1'){
            pw = true;
        }
        else if(password == 'password2'){
            npw = true;
        }
    }
    else{
        if(!document.getElementById(password).value){
            document.getElementById(password).style.color = "black";
            document.getElementById(password).style.borderColor = "black";
            if(password == 'password1'){
                pw = false;
            }
            else if(password == 'password2'){
                npw = false;
            }
        }
        else{
            document.getElementById(password).style.color = "red";
            document.getElementById(password).style.borderColor = "red";
            if(password == 'password1'){
                pw = false;
            }
            else if(password == 'password2'){
                npw = false;
            }
        }
    }
    }

        function p_check2(){
            var p1_value = document.getElementById('password2').value;
            var p2_value = document.getElementById('password3').value;
            if(p1_value == p2_value){
                document.getElementById('password3').style.color = "green";
                document.getElementById('password3').style.borderColor = "green";
                cnpw  = true
            }
            else{
                if(!document.getElementById('password3').value){
                    document.getElementById('password3').style.color = "black";
                    document.getElementById('password3').style.borderColor = "black";
                    cnpw  = false
                }
                else{
                    document.getElementById('password3').style.color = "red";
                    document.getElementById('password3').style.borderColor = "red";
                    cnpw  = false
                }
            }
        }


function Change(){
    document.getElementById("change").style.display = 'none';
    document.getElementById("submit").style.display = 'block';
    document.getElementById("password1").disabled = false;
    document.getElementById("change_password").style.display = 'block'
    document.getElementById('divMayus3').style.display = 'block';
}

function Submit(){
    var form = document.admin_form;
    console.log(pw)
    console.log(cnpw)
    console.log(npw)

    if (cnpw && npw && pw) {
        form.submit();
    }
    else{
        alert("Insufficient information")
    }
}