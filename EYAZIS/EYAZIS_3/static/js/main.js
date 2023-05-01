let request = document.getElementById('request');
let btn = document.getElementById('btn');
let block = document.getElementsByClassName('block_1')[0];
$.ajax({
    url: "load",
    type: 'POST',
    success: function(response) {
        console.log(response);
        data = response.data;
        console.log(data)
        for(let key in data){
            creating_a_user_message(key);
            creating_a_bot_message(data[key])
        }
    },
    error: function(error) {
        console.log(error);
    }
});
btn.addEventListener('click', function () {
    request.disabled = true;
    btn.disabled = true;
    creating_a_user_message(request.value)
    $.ajax({
        url: 'request',
        type: 'POST',
        data: JSON.stringify({'myData': request.value}),
        success: function(response) {
            creating_a_bot_message(response.data)
            response.data = "";
            request.value = "";
            request.disabled = false;
            btn.disabled = false;
        },
        error: function(error) {
            console.log(error);
        }
    }); 
});

function creating_a_user_message(text){
    let newSpan = document.createElement('span');
    newSpan.classList.add('span_user');
    newSpan.textContent = text;

    let newSpanDelete = document.createElement('span');
    newSpanDelete.classList.add('span_delete')
    newSpan.appendChild(newSpanDelete);
    block.appendChild(newSpan);

    newSpanDelete.addEventListener("click", function () {
        delete_message(this.parentNode)
    });
}

function creating_a_bot_message(text){
    newSpan = document.createElement('span');
    newSpan.classList.add('span_bot');
    newSpan.textContent = text;

    let newSpanDelete = document.createElement('span');
    newSpanDelete.classList.add('span_delete')
    newSpan.appendChild(newSpanDelete);
    block.appendChild(newSpan);


    newSpanDelete.addEventListener("click", function () {
        delete_message(this.parentNode)
    });
}

function delete_message(parent){
    $.ajax({
        url: 'delete',
        type: 'POST',
        data: JSON.stringify({'myData': parent.textContent}),
        success: function(response) {
            if (response.data) {
                if (parent.classList.contains("span_user")){
                    parent.nextElementSibling.remove();
                    parent.remove();
                }
                else{
                    parent.previousElementSibling.remove();
                    parent.remove();
                }
            }
        },
        error: function(error) {
            console.log(error);
        }
    }); 
}

// const childElements = document.querySelectorAll('.span_delete');

// childElements.forEach(child => {
//         child.addEventListener('click', () => {
//         const parent = child.parentNode;
//         parent.remove();
//     });
// });