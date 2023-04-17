let employees = JSON.parse(localStorage.getItem('employees'));
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');

let employee = employees[id];

function WriteName(){
    document.write(employee.empName);
}

function WriteID(){
    document.write(employee.id);
}

function WriteEmail(){
    document.write(employee.email);
}

function WriteAddress(){
    document.write(employee.address);
}

function WriteNumber(){
    document.write(employee.phone);
}

function WriteGender(){
    document.write(employee.gender);
}

function WriteStatus(){
    document.write(employee.maritalStat);
}

function WriteAvailable(){
    document.write(employee.availablePTO);
}

function WriteApproved(){
    document.write(employee.approvedPTO);
}

function WriteSalary(){
    document.write(employee.salary);
}

function WriteDate(){
    document.write(employee.DOB);
}