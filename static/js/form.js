function toggleSignup(){
    document.getElementById("login-toggle").style.backgroundColor="#fff";
     document.getElementById("login-toggle").style.color="#222";
     document.getElementById("signup-toggle").style.backgroundColor="#4574F1";
     document.getElementById("signup-toggle").style.color="#fff";
     document.getElementById("login-form").style.display="none";
     document.getElementById("signup-form").style.display="block";
 }
 
 function toggleLogin(){
     document.getElementById("login-toggle").style.backgroundColor="#4574F1";
     document.getElementById("login-toggle").style.color="#fff";
     document.getElementById("signup-toggle").style.backgroundColor="#fff";
     document.getElementById("signup-toggle").style.color="#222";
     document.getElementById("signup-form").style.display="none";
     document.getElementById("login-form").style.display="block";
 }
 function loginValidate() {
     var flag1 = true
     var flag2 = true
     un = document.getElementById('l_un');
     pwd = document.getElementById('l_pwd');
     if(un.value == ""){
         un.placeholder="this filled must not be empty"
         flag1 = false;
     }else{
         un.placeholder="Enter username"
         flag1 = true
     }
     if(pwd.value == ""){
         pwd.placeholder="this filled must not be empty"
         flag2 = false;
     }else{
         pwd.placeholder="Enter Password"
         flag2 = true
     }
     console.log(flag1);
     console.log(flag2);
     return flag1 && flag2
 }
 function signupValidate(){
     var flag1 = true
     var flag2 = true
     var flag3 = true
     var flag4 = true
     var flag5 = true
     var flag6 = true
     var flag7 = true
     fn = document.getElementById('fn');
     ln = document.getElementById('pwd');
     un = document.getElementById('un');//
     email = document.getElementById('email');//
     pwd = document.getElementById('new-pwd');//
     c_pwd = document.getElementById('conf-pwd');//
     if(un.value == ""){
         un.placeholder="this filled must not be empty"
         un.style.color="red"
         flag1 = false;
     }else{
         un.placeholder="Enter username"
         flag1 = true
     }
     if(pwd.value == ""){
         pwd.placeholder="this filled must not be empty"
         flag2 = false;
     }else{
         pwd.placeholder="Enter Password"
         flag2 = true
     }
     if(c_pwd.value == ""){
         c_pwd.placeholder="this filled must not be empty"
         c_pwd.style.color="red"
         flag3 = false;
     }else{
         c_pwd.placeholder="Enter Confirm Password"
         flag3 = true
     }
     if(email.value == ""){
         email.placeholder="this filled must not be empty"
         flag4 = false;
     }else{
         email.placeholder="Enter Email"
         flag4 = true
     }
     if(fn.value == ""){
         fn.placeholder="this filled must not be empty"
         flag5 = false;
     }else{
         fn.placeholder="Enter First Name"
         flag5 = true
     }
     if(ln.value == ""){
         ln.placeholder="this filled must not be empty"
         ln.style.color="red"
         flag6 = false;
     }else{
         ln.placeholder="Enter Last Name"
         flag6 = true
     }
     if(pwd.value != c_pwd.value){
         c_pwd.placeholder="Password and Confirm Password must be same"
         flag7 = false
     }else{
         c_pwd.placeholder="Enter Confirm Password"
         flag7 = true
     }
     console.log(flag1);
     console.log(flag2);
     console.log(flag3);
     console.log(flag4);
     console.log(flag5);
     console.log(flag6);
     console.log(flag7);
     return flag1 && flag2 && flag3 && flag4 && flag5 && flag6 && flag7
 }