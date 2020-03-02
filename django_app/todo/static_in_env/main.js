var btn = document.getElementById("btn")
var container = document.getElementById("ourcontainer")
var url = 'http://127.0.0.1:8000/api'



btn.addEventListener("click", function(){
	var ourRequest = new XMLHttpRequest();
	ourRequest.open("GET", url);
	ourRequest.onload = function() {
		var ourData = JSON.parse(ourRequest.responseText);
		renderHTML(ourData);
	}
	ourRequest.send();

})