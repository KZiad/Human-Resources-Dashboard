let employees = JSON.parse(localStorage.getItem('employees'));
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id');

let employee = employees[id];
