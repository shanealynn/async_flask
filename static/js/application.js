
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg)
        //maintain a list of ten numbers
        if (numbers_received.length >= 10){
            numbers_received.shift()
        }            
        numbers_received.push(msg.number)
        $('#log').html('<p>Current Numbers: ' + numbers_received.toString() + '</p>');
    });

});