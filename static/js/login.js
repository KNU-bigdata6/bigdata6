function capLock(e){
    kc = e.keyCode ? e.keyCode : e.which;
    sk = e.shiftKey ? e.shiftKey : ((kc == 16) ? true : false);
    if(((kc >= 65 && kc <= 90) && !sk)||((kc >= 97 && kc <= 122) && sk)){
        document.getElementById('divMayus').style.visibility = 'visible';
    }
    else{
        document.getElementById('divMayus').style.visibility = 'hidden';
    }
}
function login(){
        var form = document.login_form;
        if (form.userid.value == "") {
            alert("enter data");
        }
        else if(form.password.value == ""){
            alert("enter data");
        }
        else{
            form.submit();
        }
    }