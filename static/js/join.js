var id = false
var name = false
var pw = false
var spw = false
function capLock(e){
    kc = e.keyCode ? e.keyCode : e.which;
    sk = e.shiftKey ? e.shiftKey : ((kc == 16) ? true : false);
    if(((kc >= 65 && kc <= 90) && !sk)||((kc >= 97 && kc <= 122) && sk)){
        document.getElementById('divMayus3').style.display="none";
        document.getElementById('divMayus').style.visibility = 'visible';
        document.getElementById('divMayus2').style.visibility = 'visible';
    }
    else{
        document.getElementById('divMayus').style.visibility = 'hidden';
        document.getElementById('divMayus2').style.visibility = 'hidden';
        document.getElementById('divMayus3').style.display = "inline";
    }
    }

function p_check(){
    var pattern = /^(?=.*?[a-zA-Z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$/g;

    var value = document.getElementById('password').value;

    if (pattern.test(value)){
        document.getElementById('password').style.color = "green";
        document.getElementById('password').style.borderColor = "green";
        pw = true
    }
    else{
        if(!document.getElementById('password').value){
            document.getElementById('password').style.color = "black";
            document.getElementById('password').style.borderColor = "black";
            pw = false
        }
        else{
            document.getElementById('password').style.color = "red";
            document.getElementById('password').style.borderColor = "red";
            pw = false
        }
    }
}

function p_check2(){
    var p1_value = document.getElementById('password').value;
    var p2_value = document.getElementById('password2').value;
    if(p1_value == p2_value){
        document.getElementById('password2').style.color = "green";
        document.getElementById('password2').style.borderColor = "green";
        spw = true
    }
    else{
        if(!document.getElementById('password2').value){
            document.getElementById('password2').style.color = "black";
            document.getElementById('password2').style.borderColor = "black";
            spw = false
        }
        else{
            document.getElementById('password2').style.color = "red";
            document.getElementById('password2').style.borderColor = "red";
            spw = false
        }
    }
}

function onlykorean() {
    var pattern = /[ㄱ-ㅎ|ㅏ-ㅣ]|[a-z0-9]|[ \[\]{}()<>?|`~!@#$%^&*-_+=,.;:\"'\\]/g;
    var value = document.getElementById('username').value;
    if (pattern.test(value)) {
        document.getElementById("username").style.color = "red";
        document.getElementById("username").style.borderColor = "red";
        name = false
    }
    else{
        if(!document.getElementById("username").value){
            document.getElementById("username").style.color = "black";
            document.getElementById("username").style.borderColor = "black";
            name = false
        }
        else{
            document.getElementById("username").style.color = "green";
            document.getElementById("username").style.borderColor = "green";
            name = true
        }
    }
};

function check(){
    var q = $('#userid').val();
    if (q){
    var postdata ={
        "id" : q
    }
    var pattern = /^[a-z0-9]*$/;
    if (pattern.test(document.getElementById('userid').value))
    {
        $.ajax({
            type:'POST',
            url:'/check',
            async : true,
            data: JSON.stringify(postdata),
            dataType : 'JSON',
            contentType: "application/json",
            success: function(Check){
                let secess = Check.result2['Check'];
                if(secess){
                    alert("Sucess")
                    document.getElementById("userid").style.color = "green";
                    document.getElementById("userid").style.borderColor = "green";
                    document.getElementById("userid").readOnly = true;
                    id=true
                }
                else{
                    alert("Duplicate ID")
                    document.getElementById("userid").value = null
                }
            },
        })
    }
    else{
        alert("English lowercase and numbers only")
        document.getElementById("userid").value = null
    }
}
}
function admin(){
var form = document.admin_form;
console.log(pw)
console.log(spw)
console.log(id)
console.log(name)

if (id && name && pw && spw) {
    form.submit();
}
else{
    alert("Insufficient information")
}
}
