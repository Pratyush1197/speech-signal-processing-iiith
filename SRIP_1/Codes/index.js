let {PythonShell} = require('python-shell')
var player = require('play-sound')(opts = {})


function get_data() {
  var audio = document.getElementById("audio").value; 
  freq = document.getElementById("freq").value;
  bits = document.getElementById("bits").value;
  T = document.getElementById("T").value;
  

   

var options = {
   args: [audio, freq, bits, T],
  pythonPath: '/usr/bin/python3'
};


var tests = new PythonShell('hello.py', options);
tests.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  console.log(message);
});

 
}
function get_alias() {
 
  alias = document.getElementById("alias").value;
  
  var options2 = {
    args: [alias],
   pythonPath: '/usr/bin/python3'
 };
 
 
 var tests2 = new PythonShell('hel.py', options2);
 tests2.on('message', function (message) {
   // received a message sent from the Python script (a simple "print" statement)
   console.log(message);
 });
 
  
}
function get_sound() {
  var sound = document.getElementById("sound").value;   
player.play(sound, function(err){
  if (err) throw err
})
player.play(sound, { timeout: 3 }, function(err){
  if (err) throw err
})
}
