function checkEventHandler(event) {
    //console.log(event);
    console.log(event.target.dataset.id);
    event.target.style.textDecoration = "line-through";
    fetch("/done/"+event.target.dataset.id)
    .then(res => res.json())
    .then(data => window.location.href = data['target'])
}


var checkboxes = document.querySelectorAll('.item');
//checkboxes.forEach(checkbox => checkbox.addEventListener('touchstart',checkEventHandler, false));
//checkboxes.forEach(checkbox => checkbox.addEventListener('touchend',checkEventHandler, false));
//checkboxes.forEach(checkbox => checkbox.addEventListener('mouseup',checkEventHandler, false));
//checkboxes.forEach(checkbox => checkbox.addEventListener('mousedown',checkEventHandler, false));
//checkboxes.forEach(checkbox => checkbox.addEventListener('click',checkEventHandler, false));

setInterval(
  function(){ window.location.href = "today" },
  5*60*1000
);
