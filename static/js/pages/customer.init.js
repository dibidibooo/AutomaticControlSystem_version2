$(document).on("click", ".open_edit_modal", function(a) { a.preventDefault(); var b = $("#editProfileModal");
    a = $(this).data("popup-url");
    $(".modal-content", b).load(a, function() { b.modal("show") }) });

function editCustomer(e) { document.getElementById("uid").setAttribute("value", e), $.ajax({ data: { userid: e } }) }

function sweetDelete(e) { console.log("id" + e); const t = document.querySelector("[name=csrfmiddlewaretoken]").value;
    Swal.fire({ title: "Вы уверены?", text: "После удаления данные будут удалены навсегда!", icon: "warning", showCancelButton: !0, confirmButtonText: "Да, удалить!", cancelButtonText: "Нет, отменить!", confirmButtonClass: "btn btn-success mt-2", cancelButtonClass: "btn btn-danger ms-2 mt-2", buttonsStyling: !1 }).then((function(n) { if (n.isConfirmed) { Swal.fire({ title: "Удален", text: "Пользователь удален из базы данных!.", icon: "success" }); const n = new XMLHttpRequest,
                o = new FormData;
            o.append("id", e), o.append("deleteCustomer", "deleteCustomer"), n.open("POST", "/accounts/users"), n.setRequestHeader("X-CSRFToken", t), n.send(o), n.onload = () => { window.location.reload() } } else Swal.fire({ title: "Отмена", text: "Данные в сохранности :)", icon: "error" }) })) }