function approveVacation(id) {
  var vacations = JSON.parse(localStorage.getItem("vacations"));
  vacations[id].status = "Approved";
  localStorage.setItem("vacations", JSON.stringify(vacations));
  location.reload();
}
function denyVacation(id) {
  var vacations = JSON.parse(localStorage.getItem("vacations"));
  vacations[id].status = "Denied";
  localStorage.setItem("vacations", JSON.stringify(vacations));
  location.reload();
}
function deleteVacation(id) {
  var vacations = JSON.parse(localStorage.getItem("vacations"));
  delete vacations[id];
  localStorage.setItem("vacations", JSON.stringify(vacations));
  location.reload();
}
function loadVacCards() {
  if (
    localStorage.getItem("vacations") == null ||
    localStorage.getItem("vacations") == "{}"
  ) {
    document.write("<h1>No vacations to show</h1>");
  } else {
    let vacs = JSON.parse(localStorage.getItem("vacations"));
    let vacs_keys = Object.keys(vacs);
    for (var i = vacs_keys.length - 1; i >= 0; i--) {
      let k = vacs_keys[i];
      document.write(`<div class="vac">
                        <div class="cardHead">
                            <div class="empData">${vacs[k].id} <br/> ${vacs[k].name}</div>
                            <div class="vacStatus">Status: ${vacs[k].status}</div>
                        </div>
                        <div class="cardBody">
                            <div class="vacDates">
                                ${vacs[k].beginDate} -> ${vacs[k].endDate}
                            </div>
                            <div class="vacReason">
                                Reason: <br/> ${vacs[k].reason}
                            </div>
                            <div class="vacActions">
                                <button class="appBut" onclick="approveVacation(${k})">Approve</button>
                                <button class="denBut" onclick="denyVacation(${k})">Deny</button>
                                <button class="deleteBut" onclick="deleteVacation(${k})">Delete</button>
                            </div>
                        </div>
                    </div>`);
    }
  }
}
