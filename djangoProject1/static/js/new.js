
function checkForm()
{
    var lab_id=document.getElementById("lab_id").value;
    var lab_name=document.getElementById("lab_name").value;
    var lab_num=document.getElementById("lab_num").value;
    var floor_num=document.getElementById("floor_num").value;
    var pc_num=document.getElementById("pc_num").value;
    var lab_cap=document.getElementById("lab_cap").value;
    var chair_num=document.getElementById("chair_num").value;
    
    if(lab_name=="")
    {
        alert("ERROR:you should write the name");
        document.getElementById("lab_name").focus();
        return false;
    }
    if(lab_id=="")
    {
        alert("ERROR:you should write the laboratory id");
        document.getElementById("lab_id").focus();
        return false;
    }
    if(lab_num=="")
    {
        alert("ERROR:you should write the laboratory number");
        document.getElementById("lab_num").focus();
        return false;
    }
    if(floor_num=="")
    {
        alert("ERROR:you should write the floor number");
        document.getElementById("floor_num").focus();
        return false;
    }
    if(pc_num=="")
    {
        alert("ERROR:you should write the PC number");
        document.getElementById("pc_num").focus();
        return false;
    }
    if(lab_cap=="")
    {
        alert("ERROR:you should write the laboratory capacity");
        document.getElementById("lab_cap").focus();
        return false;
    }
    if(chair_num=="")
    {
        alert("ERROR:you should write the chair number");
        document.getElementById("chair_num").focus();
        return false;
    }
    if (status_1!=value)
    {
        alert("ERROR:you should write the status");
        document.getElementById("stat_1").focus();
        return false;
    }
    if (status_2!=value)
    {
        alert("ERROR:you should write the status");
        document.getElementById("stat_2").focus();
        return false;
    }
}
