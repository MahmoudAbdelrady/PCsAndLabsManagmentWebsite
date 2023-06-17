function checkForm()
{
    var pc_id=document.getElementById("pc_id").value;
    var lab_id=document.getElementById("lab_id").value;
    var stat_1=document.getElementById("stat_1").value;
    var stat_2=document.getElementById("stat_2").value;

    
    if(lab_id=="")
    {
        alert("ERROR:you should write the laboratory id");
        document.getElementById("lab_name").focus();
        return false;
    }
    if(pc_id=="")
    {
        alert("ERROR:you should write the pc id");
        document.getElementById("lab_id").focus();
        return false;
    }
    if(stat_1!=RadioNode)
    {
        alert("ERROR:you should write the pc id");
        document.getElementById("lab_id").focus();
        return false;
    }
}