let employees = JSON.parse(localStorage.getItem('employees'));

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');
const employee = employees[id];

 // FILL THE FORM
document.getElementById('id').value = id;
document.getElementById('name').value = employee.empName;
document.getElementById('maleRadio').checked = employee.gender == "Male";
document.getElementById('femaleRadio').checked = employee.gender == "Female";
document.getElementById('email').value = employee.email;
document.getElementById('address').value = employee.address;
document.getElementById('number').value = employee.phone;
document.getElementById('dob').valueAsDate = new Date(employee.DOB);
document.getElementById('maritalStat').value = employee.maritalStat;
document.getElementById('availablePTO').value = employee.availablePTO;
document.getElementById('approvedPTO').value = employee.approvedPTO;
document.getElementById('salary').value = employee.salary;

// UPDATE FORM 
const updateButton = document.getElementById('update-button');
updateButton.addEventListener('click', function() {
  employee.empName = document.getElementById('name').value;
  employee.gender = document.querySelector('input[name = "gender"]:checked') ? document.querySelector('input[name = "gender"]:checked').value : null;
  employee.email = document.getElementById('email').value;
  employee.address = document.getElementById('address').value;
  employee.number = document.getElementById('number').value;
  employee.DOB = document.getElementById('dob').value;
  employee.maritalStat = document.getElementById('maritalStat').value;
  employee.availablePTO = document.getElementById('availablePTO').value;
  employee.salary = document.getElementById('salary').value;
  employees[id] = employee;
  localStorage.setItem('employees', JSON.stringify(employees));
  alert('Employee updated successfully!');
  window.location.href = 'index.html';
});

// DELETE EMPOLYEE
const deleteButton = document.getElementById('delete-button');
deleteButton.addEventListener('click', function() {
  delete employees[id];
  localStorage.setItem('employees', JSON.stringify(employees));
  alert('Employee deleted successfully!');
  window.location.href = 'index.html';
});

