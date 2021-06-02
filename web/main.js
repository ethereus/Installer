//
// main.js
// Package Installer
//
// Created by Yuna on 19/02/21
// Copyright © 2021 Yuna. All rights reserved.
//

//   NOTE TO SELF:
//
//   USE ABSOLUTE POSITION TO LAYER ELEMENTS OVER EACH OTHER AND THEN HIDE/SHOW WHEN NEEDED
//

async function downloadPackage() {

	var a = document.getElementById("package");
	a.style.display = "none";

	var b = document.getElementById("submit2");
	b.style.display = "none";

	var c = document.getElementById("removeChoice");
	c.style.display = "none";

	var d = document.getElementById("submit3");
	d.style.display = "none";

	var e = document.getElementById("repoNew");
	e.style.display = "none";

	var f = document.getElementById("submit4");
	f.style.display = "none"; 

	var g = document.getElementById("repoChosen");
	g.style.display = "none";

	var h = document.getElementById("submit5");
	h.style.display = "none"; 

	var j = document.getElementById("updateButton");
	j.style.display = "none";

	var k = document.getElementById("repoChoice");
	k.style.display = "none";

	var l = document.getElementById("submit");
	l.style.display = "none"; 

	document.getElementById("text").innerHTML = "";

	document.getElementById("repoText").innerHTML = "Repository List";

	var y = document.getElementById("repoChoice");
	y.style.display = "block";

	var z = document.getElementById("submit");
	z.style.display = "block";
            
	// Call into Python so we can access the data
	let info = await eel.button1()();

	var i = 0;
	var len = info.length;
	var text = "";

	for (; i < len; ) {
	  text += info[i] + "<br>";
	  i++;

	document.getElementById("text").innerHTML = text;

	}
              
}

async function removeButton() {

	var a = document.getElementById("package");
	a.style.display = "none";

	var b = document.getElementById("submit2");
	b.style.display = "none";

	var c = document.getElementById("removeChoice");
	c.style.display = "none";

	var d = document.getElementById("submit3");
	d.style.display = "none";

	var e = document.getElementById("repoNew");
	e.style.display = "none";

	var f = document.getElementById("submit4");
	f.style.display = "none"; 

	var g = document.getElementById("repoChosen");
	g.style.display = "none";

	var h = document.getElementById("submit5");
	h.style.display = "none"; 

	var j = document.getElementById("updateButton");
	j.style.display = "none";

	var k = document.getElementById("repoChoice");
	k.style.display = "none";

	var l = document.getElementById("submit");
	l.style.display = "none"; 

	document.getElementById("text").innerHTML = "";
	
	document.getElementById("repoText").innerHTML = "Installed Packages: ";
            
	// Call into Python so we can access the data
	let check = await eel.choosePackageRemove()();

	if (check == 0) {

	  document.getElementById("text").innerHTML = "No Packages Currently Installed";

	} else {

	  var y = document.getElementById("removeChoice");
	  y.style.display = "block";

	  var z = document.getElementById("submit3");
	  z.style.display = "block";

	  var i = 0;
	  var len = check.length;
	  var text = "";

	  for (; i < len; ) {
	    text += check[i] + "<br>";
	    i++;
	  }

	  document.getElementById("text").innerHTML = text;
              
   }  

}

async function removePackage() {

	var choice = document.getElementById("removeChoice").value;
            
	// Call into Python so we can access the data
	let check = await eel.startRemove(choice)();

	if (check == 1) {

	  document.getElementById("repoText").innerHTML = "Package Removed";

	  var x = document.getElementById("removeChoice");
	  x.style.display = "none";

	  var z = document.getElementById("submit3");
	  z.style.display = "none";

	  document.getElementById("text").innerHTML = "";

	}   

}

async function addrepoButton() {

	var a = document.getElementById("package");
	a.style.display = "none";

	var b = document.getElementById("submit2");
	b.style.display = "none";

	var c = document.getElementById("removeChoice");
	c.style.display = "none";

	var d = document.getElementById("submit3");
	d.style.display = "none";

	var e = document.getElementById("repoNew");
	e.style.display = "none";

	var f = document.getElementById("submit4");
	f.style.display = "none"; 

	var g = document.getElementById("repoChosen");
	g.style.display = "none";

	var h = document.getElementById("submit5");
	h.style.display = "none"; 

	var j = document.getElementById("updateButton");
	j.style.display = "none";

	var k = document.getElementById("repoChoice");
	k.style.display = "none";

	var l = document.getElementById("submit");
	l.style.display = "none"; 

	document.getElementById("text").innerHTML = "";

	document.getElementById("text").innerHTML = "";

	document.getElementById("repoText").innerHTML = "Add Repo";
    
    var y = document.getElementById("repoNew");
	y.style.display = "block";

	var z = document.getElementById("submit4");
	z.style.display = "block";

}

async function addRepo() {

	var input = document.getElementById("repoNew").value;
            
	// Call into Python so we can access the data
	let check = await eel.addRepo(input)();

	if (check == 0) {

	  document.getElementById("text").innerHTML = "";

	} else {

		document.getElementById("repoText").innerHTML = "Source Added";

		var x = document.getElementById("repoNew");
	    x.style.display = "none";

	    var z = document.getElementById("submit4");
	    z.style.display = "none";

	}

}

async function removerepoButton() {

	var a = document.getElementById("package");
	a.style.display = "none";

	var b = document.getElementById("submit2");
	b.style.display = "none";

	var c = document.getElementById("removeChoice");
	c.style.display = "none";

	var d = document.getElementById("submit3");
	d.style.display = "none";

	var e = document.getElementById("repoNew");
	e.style.display = "none";

	var f = document.getElementById("submit4");
	f.style.display = "none"; 

	var g = document.getElementById("repoChosen");
	g.style.display = "none";

	var h = document.getElementById("submit5");
	h.style.display = "none"; 

	var j = document.getElementById("updateButton");
	j.style.display = "none";

	var k = document.getElementById("repoChoice");
	k.style.display = "none";

	var l = document.getElementById("submit");
	l.style.display = "none"; 

	document.getElementById("text").innerHTML = "";

	document.getElementById("repoText").innerHTML = "Remove Repo";
            
	// Call into Python so we can access the data
	let check = await eel.removerepoCheck()();

	if (check == 0) {

	  document.getElementById("text").innerHTML = "No Sources Currently Installed";

	} else {

		var x = document.getElementById("repoChosen");
	    x.style.display = "block";

	    var z = document.getElementById("submit5");
	    z.style.display = "block";

	    getRemoveRepo()

	}

}

async function getRemoveRepo() {
            
	// Call into Python so we can access the data
	let x = await eel.repoListSend()();

	var i = 0;
	var len = x.length;
	var text = "";

	for (; i < len; ) {
	  text += x[i] + "<br>";
	  i++;
	}

	
	document.getElementById("text").innerHTML = text;

}

async function submitRepo() {

	var input = document.getElementById("repoChosen").value;
            
	eel.removeRepo(input);

	document.getElementById("repoText").innerHTML = "Source Removed";

	var x = document.getElementById("repoChosen");
	x.style.display = "none";

	var z = document.getElementById("submit5");
	z.style.display = "none";

	document.getElementById("text").innerHTML = "";

}

async function submit() {

	var input = document.getElementById("repoChoice").value;

	eel.data(input);

	document.getElementById("repoText").innerHTML = "Packages in repo: ";

	var y = document.getElementById("repoChoice");
	y.style.display = "none";

	var z = document.getElementById("submit");
	z.style.display = "none";

	packages_list();

}

async function packages_list() {

	var y = document.getElementById("package");
	y.style.display = "block";

	var z = document.getElementById("submit2");
	z.style.display = "block";

	let x = await eel.packages_list_step()();

	var i = 0;
	var len = x.length;
	var text = "";

	for (; i < len; ) {
	  text += x[i] + "<br>";
	  i++;
	}

	
	document.getElementById("text").innerHTML = text;

}

async function updateButton() {

	var a = document.getElementById("package");
	a.style.display = "none";

	var b = document.getElementById("submit2");
	b.style.display = "none";

	var c = document.getElementById("removeChoice");
	c.style.display = "none";

	var d = document.getElementById("submit3");
	d.style.display = "none";

	var e = document.getElementById("repoNew");
	e.style.display = "none";

	var f = document.getElementById("submit4");
	f.style.display = "none"; 

	var g = document.getElementById("repoChosen");
	g.style.display = "none";

	var h = document.getElementById("submit5");
	h.style.display = "none"; 

	var j = document.getElementById("updateButton");
	j.style.display = "none";

	var k = document.getElementById("repoChoice");
	k.style.display = "none";

	var l = document.getElementById("submit");
	l.style.display = "none"; 

	document.getElementById("text").innerHTML = "";

	document.getElementById("repoText").innerHTML = "Update Packages";

	let check = await eel.checkUpdates()();

	if (check == 0) {

	    document.getElementById("text").innerHTML = "No Updates Available";

	} else {

		document.getElementById("repoText").innerHTML = "Updates Available: ";

		update = check

		var i = 0;
	    var len = check.length;
	    var text = "";

	    for (; i < len; ) {
	      text += check[i] + "<br>";
	      i++;
	    }

	
	document.getElementById("text").innerHTML = text;

	var x = document.getElementById("updateButton");
	x.style.display = "block";

	}

	
	document.getElementById("text").innerHTML = text;

}

async function updateGo() {

	let updates = await eel.checkUpdates()();

	eel.updatePackages(updates)

	document.getElementById("repoText").innerHTML = "Done";

	document.getElementById("text").innerHTML = "Packages Are Up To Date";

	var x = document.getElementById("updateButton");
	x.style.display = "none";

}

async function submitChoice() {

	var input = document.getElementById("package").value;

	eel.find_id(input);

	document.getElementById("repoText").innerHTML = "Download Complete";

	var x = document.getElementById("package");
	x.style.display = "none";

	var z = document.getElementById("submit2");
	z.style.display = "none";

	document.getElementById("text").innerHTML = "";

}
