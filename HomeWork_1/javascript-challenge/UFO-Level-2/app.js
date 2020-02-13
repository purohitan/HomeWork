// Get references to the tbody element, input fields and button
var $tbody = document.querySelector("tbody");
var $dateInput = document.querySelector("#datetime");
var $stateInput = document.querySelector("#state");
var $cityInput = document.querySelector("#city");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");
var $resetBtn = document.querySelector("#reset");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Add an event listener to the resetButton, call handleResetButtonClick when clicked
$resetBtn.addEventListener("click", handleResetButtonClick);

// Create a copy of the data
var tableData = data;

// Build table with non-filtered data
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < tableData.length; i++) {
    // Get current address object and fields
    var address = tableData[i];
    console.log(address)
    var fields = Object.keys(address);
    // Create new row in tbody, set index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For each field in address object, create new cell and set inner text to be current value at current address field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = address[field];
    }
  }
}

// Build search table for filtered data
function handleSearchButtonClick() {
  var filterDate = $dateInput.value;
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();

  // Filter on date
  if (filterDate != "") {
    tableData = data.filter(function (address) {
      var addressDate = address.datetime;
      return addressDate === filterDate;
    });
  }
  else { tableData };

  // Filter on state
  if (filterState != "") {
    tableData = tableData.filter(function (address) {
      var addressState = address.state;
      return addressState === filterState;
    });
  }
  else { tableData };

  // Filter on city
  if (filterCity != "") {
    tableData = tableData.filter(function (address) {
      var addressCity = address.city;
      return addressCity === filterCity;
    });
  }
  else { tableData };

  // Filter on country
  if (filterCountry != "") {
    tableData = tableData.filter(function (address) {
      var addressCountry = address.country;
      return addressCountry === filterCountry;
    });
  }
  else { tableData };

  // Filter on shape
  if (filterShape != "") {
    tableData = tableData.filter(function (address) {
      var addressShape = address.shape;
      return addressShape === filterShape;
    });
  }
  else { tableData };

  renderTable();
}

// Clear all the fields
function handleResetButtonClick(){
  renderTable();
}

// Render the table for the first time on page load
renderTable();