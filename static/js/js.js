// JQuery - Data máxima = dia de hoje.
var today = new Date().toISOString().split('T')[0];
$(".data").attr('max', today);