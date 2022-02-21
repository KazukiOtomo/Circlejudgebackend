document.getElementById("go-back").addEventListener("click", () => {
  history.back();
});

// home
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
  let sql_text = "";
  let doSQLelement = document.getElementById("doSQLBtn");
  doSQLelement.classList.remove("btn-primary");
  doSQLelement.classList.remove("btn-danger");
  if (checkValue == "SELECT") {
    sql_text = "SELECT * FROM " + db_name;
    document.getElementById("sql_textarea").style.color = "black";
    doSQLelement.classList.add("btn-primary");
  } else {
    sql_text = "DELETE FROM " + db_name;
    document.getElementById("sql_textarea").style.color = "red";
    doSQLelement.classList.add("btn-danger");
  }
  document.getElementById("sql_textarea").value = sql_text;
}
