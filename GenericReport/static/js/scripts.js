let button = document.getElementById('add')
let form = document.querySelector('.form')
let forms = document.getElementById('forms')

button.addEventListener("click", function() {
    console.log('Add')
    clone = form.cloneNode(true)
    forms.appendChild(clone)
});
// remove_button.onclick = () => {
//     const myNode = form.cloneNode(true)
//     myNode.innerHTML = '';
//   }

$(".deleteButton").click(function(){
    if($('.deleteButton').length > 1){

       $(this).closest("tr").remove();
    }

});