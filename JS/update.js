let employees = JSON.parse(localStorage.getItem('employees'));

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');
const employee = employees[id];
 // FILL THE FORM
document.getElementById('id').value = employee.id;
document.getElementById('name').value = employee.name;
document.getElementById('email').value = employee.email;
document.getElementById('address').value = employee.address;
document.getElementById('number').value = employee.number;
document.getElementById('dob').value = employee.dob;
document.getElementById('status').value = employee.status;
document.getElementById('vacation-days').value = employee.vacationDays;
document.getElementById('approved-vacation-days').value = employee.approvedVacationDays;
document.getElementById('salary').value = employee.salary;

// UPDATE FORM 

const updateButton = document.getElementById('update-button');
updateButton.addEventListener('click', function() {
  employee.name = document.getElementById('name').value;
  employee.email = document.getElementById('email').value;
  employee.address = document.getElementById('address').value;
  employee.number = document.getElementById('number').value;
  employee.dob = document.getElementById('dob').value;
  employee.status = document.getElementById('status').value;
  employee.vacationDays = document.getElementById('vacation-days').value;
  employee.approvedVacationDays = document.getElementById('approved-vacation-days').value;
  employee.salary = document.getElementById('salary').value;
  employees[id] = employee;
  localStorage.setItem('employees', JSON.stringify(employees));
  window.location.href = 'index.html';
});

// DELETE EMPOLYEE
const deleteButton = document.getElementById('delete-button');
deleteButton.addEventListener('click', function() {
  delete employees[id];
  localStorage.setItem('employees', JSON.stringify(employees));
  window.location.href = 'index.html';
});

// FOR CANCEL 
window.location.href = 'index.html';
