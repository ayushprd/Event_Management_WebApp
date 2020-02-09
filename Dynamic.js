var data='<div class="container countdown"><h1>Countdown to my birthday:</h1><ul><li class="countli"><span id="days"></span>days</li><li><span id="hours"></span>Hours</li><li><span id="minutes"></span>Minutes</li><li><span id="seconds"></span>Seconds</li></ul></div>';
var modal='<div class="modal fade container-fluid" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered" role="document"><div class="modal-content">    <div class="modal-header"><h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5><button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button></div><div class="modal-body">...</div><div class="modal-footer footer">'+data+'<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button><button type="button" class="btn btn-primary">Remind Me</button></div></div></div></div>';
var card='<div class="card mb-4 text-black bg-light">'+
            '<img class="card-img-top" src="sample.jpg" alt="Card image">'+
                '<div class="card-body">'+
                    '<h4 class="card-title">Rohan Prasad</h4>'+
                    '<p class="card-text">Sample text.</p>'+
                    '<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter">Read More</button>'+
                '</div>'+
            '</div>';

card=card+modal;
var klass='<div class="card mx-auto">';
var path = window.location.pathname;
var page = path.split("/").pop();
console.log( page );

var place=document.getElementById("wrapper");   
deck=[];
myFunction();
function myFunction(){
    deck.push(card);
    var len=deck.length;
    console.log(deck);
    if(len==1){
        place.className="mx-auto";
    }else if(len>3){
        place.className="my-auto d-md-inline-flex align-self-sm-center";
    }
    document.getElementById("wrapper").innerHTML = deck.join('');

    console.log(card);   
}





$( document ).ready(function() {
    const second = 1000,
      minute = second * 60,
      hour = minute * 60,
      day = hour * 24;

let countDown = new Date('Sep 30, 2020 00:00:00').getTime(),
    x = setInterval(function() {

      let now = new Date().getTime(),
          distance = countDown - now;

      document.getElementById('days').innerText = Math.floor(distance / (day)),
        document.getElementById('hours').innerText = Math.floor((distance % (day)) / (hour)),
        document.getElementById('minutes').innerText = Math.floor((distance % (hour)) / (minute)),
        document.getElementById('seconds').innerText = Math.floor((distance % (minute)) / second);
      
      //do something later when date is reached
      //if (distance < 0) {
      //  clearInterval(x);
      //  'IT'S MY BIRTHDAY!;
      //}

    }, second)     
});
