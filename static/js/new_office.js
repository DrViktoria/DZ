 function showError(container, errorMessage) {
      container.className = 'error';
      var msgElem = document.createElement('span');
      msgElem.className = "error-message";
      msgElem.innerHTML = errorMessage;
      container.appendChild(msgElem);
    }

function resetError(container) {
      container.className = '';
      if (container.lastChild.className == "error-message") {
        container.removeChild(container.lastChild);
      }
    }

function validate(form) {
    var elems = form.elements;

    resetError(elems.named.parentNode);
    if (!elems.named.value){
        showError(elems.named.parentNode, 'укажите название')
    }

    resetError(elems.location.parentNode);
    if (!elems.location.value){

    }
}