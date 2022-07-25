$(document).on("click", ".open_task", function (e) {
    e.preventDefault();
    let $popup = $("#staticBackdrop");
    let popup_url = $(this).data("popup-url");
    $(".modal-content", $popup).load(popup_url, function () {
      $popup.modal("show");
    });
});
function editTask(event){
    let task_id = document.getElementById("uid");
    task_id.setAttribute("value", event);
    $.ajax({
        type: 'GET',
        data: {
            'taskid': event
        },
        success: function (result) {
            console.log('Success!');
        },
        error: function (result) {
            console.log('Error!');
        }
    });
}