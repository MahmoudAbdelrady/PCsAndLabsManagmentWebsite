const form = document.getElementById('form');
const labID = document.getElementById('labID');
const email = document.getElementById('email');
const NumPc = document.getElementById('NumPc');
const problemtype = document.getElementById('problemtype');


const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};



document.forms[0].onsubmit=function (e) {
    const labIDValue = labID.value.trim();
    const NumPcValue = NumPc.value.trim();
    const problemtypeValue = problemtype.value.trim();

    let labIdValid=false;
    let numPcValid=false;
    let problemtypeValid=false;


    if(labIDValue === '') {
        setError(labID, 'labID is required');
    } 
    else if (isNaN( labIDValue )) {
        setError(labID, 'labID must be number.');
    } 
    else {
        setSuccess(labID);
        labIdValid=true;
    }


    if(NumPcValue === '') {
        setError(NumPc, 'NumPc is required');
    } else if (isNaN( NumPcValue )) {
        setError(NumPc, 'NumPc must be number.');
    } else {
        setSuccess(NumPc);
        numPcValid=true;
    }

  if(problemtypeValue == "-1" ) {
      setError(problemtype, 'Please provide your problem type!');
   }
   else{
    setSuccess(problemtype);
    problemtypeValid=true;
   }

   if(labIdValid===false || numPcValid===false || problemtypeValid===false){
      e.preventDefault(); 
   }

};
