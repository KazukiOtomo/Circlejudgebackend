document.getElementById("go-back").addEventListener("click", () => {
  history.back();
});

// home
// 初期化
document.getElementById("checkDoSQL").style.display = "none";

function appendText(db_name) {
  let checkValue = "";
  let fruitRadio = document.getElementsByName("flexRadioDefault");
  let len = fruitRadio.length;
  for (let i = 0; i < len; i++) {
    if (fruitRadio.item(i).checked) {
      checkValue = fruitRadio.item(i).value;
    }
  }
  //
  const p1 = document.getElementById("checkDoSQL");
  //
  let sql_text = "";
  let doSQLelement = document.getElementById("doSQLBtn");
  doSQLelement.classList.remove("btn-primary");
  doSQLelement.classList.remove("btn-danger");
  if (checkValue == "SELECT") {
    sql_text = "SELECT * FROM " + db_name;
    document.getElementById("sql_textarea").style.color = "black";
    doSQLelement.classList.add("btn-primary");
    doSQLelement.removeAttribute("disabled");
    p1.style.display = "none";
  } else {
    sql_text = "DELETE FROM " + db_name;
    document.getElementById("sql_textarea").style.color = "red";
    doSQLelement.classList.add("btn-danger");
    doSQLelement.setAttribute("disabled", "true");
    //
    p1.style.display = "block";
    //
    var allowDrinksCheckbox = document.getElementById("flexCheckDefault");
    var drinkSelect = document.getElementById("doSQLBtn");

    allowDrinksCheckbox.addEventListener(
      "change",
      function (event) {
        if (event.target.checked) {
          drinkSelect.removeAttribute("disabled");
        } else {
          drinkSelect.setAttribute("disabled", "true");
        }
      },
      false
    );
  }
  document.getElementById("sql_textarea").value = sql_text;
}
