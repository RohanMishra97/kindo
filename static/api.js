function checkEventHandler(event) {
    console.log(event.target.dataset.id);
    event.target.parentElement.parentElement.style.textDecoration = "line-through";
    fetch("/done/"+event.target.dataset.id)
    .then(res => res.json())
    .then(data => window.location.href = data['target'])
}


var checkboxes = document.querySelectorAll('.check-box');
checkboxes.forEach(checkbox => checkbox.addEventListener('click',checkEventHandler, false));
