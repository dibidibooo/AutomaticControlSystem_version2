$(document).ready(function () {

    $("#pricerange").ionRangeSlider({
        skin: "square",
        type: "double",
        grid: true,
        min: 0,
        max: 1000,
        from: 200,
        to: 800,
        prefix: "$"
    });

});