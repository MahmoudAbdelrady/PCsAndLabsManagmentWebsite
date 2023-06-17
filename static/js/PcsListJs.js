function change(){
    document.getElementById("Editbtn").style.display='none';
    document.getElementById("Savebtn").style.display='block';
    var len = x = document.getElementsByClassName("mainst").length;
    for(let i = 0 ; i<len ; i++){
        document.getElementsByClassName("mainst")[i].style.display='none';
        document.getElementsByClassName("stchng")[i].style.display='block';
    }
}
function save(){
    document.getElementById("Editbtn").style.display='block';
    document.getElementById("Savebtn").style.display='none';
    var len = x = document.getElementsByClassName("mainst").length;
    for(let i = 0 ; i<len ; i++){
        document.getElementsByClassName("mainst")[i].innerHTML = 
        document.getElementsByClassName("stchng")[i].value;
    }
    for(let i = 0 ; i<len ; i++){
        document.getElementsByClassName("mainst")[i].style.display='block';
        document.getElementsByClassName("stchng")[i].style.display='none';
    }
}