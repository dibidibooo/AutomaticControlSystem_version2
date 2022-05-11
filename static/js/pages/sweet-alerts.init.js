! function(t) {
    "use strict";

    function e() {}
    e.prototype.init = function() {
         t("#sa-custom").click(function() {
            Swal.fire({
                icon: "success",
                title: "<b>Результат загружен в базу</b>",
                showConfirmButton: !1,
                timer: 3000
            })
        })
    }, t.SweetAlert = new e, t.SweetAlert.Constructor = e
}(window.jQuery),
function() {
    "use strict";
    window.jQuery.SweetAlert.init()
}();